import grpc
from concurrent import futures
from datetime import datetime

import tracking_pb2
import tracking_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = tracking_pb2_grpc.TrackingServiceStub(channel)

print("Weclome to SafeEntry")

print()
print("LOGIN")

name = input("Enter your Name: ")
nric = input("Enter your NRIC: ")
print()
location = None

loop = True
option = None

def login(name, nric):
    auth = stub.Login(tracking_pb2.User(name=name,nric=nric))
    print("####################")
    if auth.status.status is False:
        print("Incorrect Login Details")
        return None
    else:
        print("Succesfully Login")
        print("Welcome " + name)
        print("Current Role: " + auth.role_name)
        print()
        return auth.role_name

def selectLocation():
    print()
    locations_list = getAllLocations()
    for count, location in enumerate(locations_list):
        print(str(count+1) + " " + location.name)
    print()
    # If no location options is available
    if str(len(locations_list)) == "0":
        print("No location Options Available")
        return None 
    # Get User input on location
    else:
        print("ENTER LOCATION")
        i = input("Select Option 1 to " + str(len(locations_list)) + ": ")
    if int(i) > len(locations_list):
        return None 
    else:
        print()
        print("Selected Location: " + locations_list[int(i)-1].name)
        return locations_list[int(i)-1]

def getAllLocations():
    print("####################")
    print("LISTING ALL LOCATIONS")
    return list(stub.GetAllLocations(tracking_pb2.Empty()))

# Note: Here has location
def checkInIndivudal(location):
    result = stub.CreateCheckInIndividual(tracking_pb2.Location(
        user = tracking_pb2.User(name = name),
        name = location
    ))
    if result.status is False:
        print("Individual Check in Failed")
        return False
    else:
        print("Individual Checked in succesfully to " + location)
        return True

# Note: Here has location and group
def checkInGroup(location, group):
    print()
    result = stub.CreateCheckInGroup(tracking_pb2.Location(
        name = location,
        group = tracking_pb2.Group(name = group)
    ))
    if result.status is False:
        print("Group Check in Failed")
        return False
    else:
        print("Group Checked in succesfully to " + location)
        return True


def selectGroup():
    groups_list = list(stub.GetGroupsByUser(tracking_pb2.User(name=name)))
    print("LISTING GROUPS")
    for count, group in enumerate(groups_list):
        print(str(count+1) + ": " + group.name)
    print()
    # If no group options is available
    if str(len(groups_list)) == "0":
        print("No Checkout Options Available")
        return None
    # Get user input on group options
    else:
        print("Enter a group you would like in check in to")
        i = input("Select Option 1 to " + str(len(groups_list)) + ": ")
    if int(i) > len(groups_list):
        return None 
    else:
        print()
        print("Selected Group: " + groups_list[int(i)-1].name)
        return groups_list[int(i)-1].name

def getCheckOutOptions():
    print()
    print("Listing Check Out Options")
    print()
    print("### INDIVIDUAL CHECK OUT OPTION ###")
    print("###################################")
    checkout_list_individual = list(stub.GetCheckOutOptionsIndividual(
        tracking_pb2.User(name = name))
    )
    # Counter to Count No of Options; Individual + Group
    counter = 0
    for check_out in checkout_list_individual:
        counter += 1
        print(str(counter) + " Location: "  + check_out.location.name)
        print("Check-in: " + str(check_out.check_in))
        print()

    print("### GROUP CHECK OUT ###")
    print("#######################")
    check_out_group = list(stub.GetCheckOutOptionsGroup(
        tracking_pb2.User(name = name))
    )
    for check_out in check_out_group:
        counter += 1
        print(str(counter) + " Location: "  + check_out.location.name)
        print("Check-in: " + str(check_out.check_in))
        print("Group: " + check_out.group.name)
        print()

    # If no check out options available
    if counter == 0:
        print("No Checkout Options Available")
        return None
    else:
        print("Enter a option to check out to")
        i = input("Select Option 1 to " + str(counter) + ": ")
    
    if int(i) > counter or int(i) <= 0 :
        return None
    else:
        print()
        if int(i) <= len(checkout_list_individual):
            # Check out indiviudal
            status = checkOutIndivudal(checkout_list_individual[int(i)-1].id)
            return status
        else:
            # Offset the option from the check out individual
            offset = int(i) - len(checkout_list_individual) - 1
            status = checkOutGroup(check_out_group[offset])
            return status
        

def checkOutIndivudal(id):
    result = stub.CreateCheckOutIndividual(tracking_pb2.CheckOut(id=id))
    if result.status is False:
        print("Individual Check out Failed")
        return False
    else:
        print("Individual Check out succesful")
        return True

def checkOutGroup(checkOut):
    result = stub.CreateCheckOutGroup(tracking_pb2.CheckOut(
       location = tracking_pb2.Location(name = checkOut.location.name),
       check_in = checkOut.check_in,
       group = tracking_pb2.Group(name = checkOut.group.name)
    ))
    if result.status is False:
        print("Group Check out Failed")
        return False
    else:
        print("Group Check out succesful")
        return True

def createGroup(group_name):
    print()
    group_name = input("Enter the new group name: ")
    print("Enetered group name", group_name)
    result = stub.CreateGroup(tracking_pb2.Group(
        name = group_name,
        user = tracking_pb2.User(name = name)))
    if(result.status.status):
        addUserToGroup(result.name)
        return None
    else:
        print("Group name exist")
        createGroup(group_name)

def addUserToGroup(group_name):
    loop = True
    user_list = list()
    while loop:
        print()
        print("Options")
        print("1: Include user to group")
        print("2: Finish Adding Users")

        option = input("Enter your Option: ")

        if option == "1":
            print()
            print("Users to be included: ")
            for user in user_list:
                print(user, end=', ')
            # List all users except currentuser
            selected_user = selectUser()
            # Append users to list
            if selected_user not in user_list:
                user_list.append(selected_user)
            else:
                print("User is already included")
            pass 
        elif option == "2":
            # Add users to group
            def handler():
                for user in user_list:
                    yield tracking_pb2.User(
                        name = user,
                        group = tracking_pb2.Group(name = group_name)
                    )
            status = stub.AddUserToGroup(handler())
            user_list = [] 

            # End loop
            loop = False
        else:
            print("Please enter a valid option")
    return None

def selectUser():
    print()
    user_list = getAllUser()
    for count, user in enumerate(user_list):
        print(str(count+1) + ": " + user.name)
    print()
    if str(len(user_list)) == "0":
        print("No User Options Available")
        return None
    else:
        print("Enter a user option ")
        i = input("Select Option 1 to " + str(len(user_list)) + ": ")
    if int(i) > len(user_list):
        return None
    else:
        print()
        print("Selected Check out Option: " + i)
        return user_list[int(i)-1].name

def getAllUser():
    return list(stub.GetAllUsers(tracking_pb2.User(name = name)))

def getSafeEntryHistory():
    print("### SAFEENTRY HISTORY ###")
    print("#########################")
    for count, row in enumerate(stub.GetSafeEntry(tracking_pb2.User(name = name))):
        print(str(count+1) + ": Location: " + row.location.name)
        print("Check in: " + row.checkin)
        print("Check out: " + row.checkout)
        print()

def getCovidLocationByUser(name):
    print()
    print("Self Reporting")
    def handler():
        location_list = list(stub.GetCovidLocationByUser(tracking_pb2.User(name=name)))
        if len(location_list) == 0:
            print("User did not visit any locations in the past 14 days")
        for location in location_list:
            print("Notificiation will be sent to people who visited " + location.name)
            yield tracking_pb2.Location(id = location.id)
    createCovidCase(handler)

def createCovidCase(location_handler):
    # Check if there is mutiple location; whether request is a stream
    if callable(location_handler):
        status = stub.CreateReportCovidCase(location_handler())
        return status.status
    else:
        # Need to get id from LOCATION HERE
        def handler():
            for id in [location_handler]:
                yield tracking_pb2.Location(id=id)
        status = stub.CreateReportCovidCase(handler())
        return status.status

def getNotificiationByUser():
    print()
    print("### LISTING NOTIFICIATION OF COVID CONTACT ###")
    print("#############################")
    for count, row in enumerate(stub.GetAllNotificiationByUser(tracking_pb2.User(name=name))):
        print(str(count+1) + " : Location: " + row.location.name)
        print("Case Occurance: " + row.case_date)
        print("Check in Date: " + row.check_in)
        print("Check Out Date: " + row.check_out)
        print()

    print("Please monitor your health and do not travel outside")

role = login(name, nric)

if role is not None:
    
    while loop: 
        print()
        print("####################")

        # Options depending on user roles
        if role == "Normal":
            print("Options")
            print("1: Check in ")
            print("2: Check Out")
            print("3: Create Group")
            print("4: List SafeEntry")
            print("5: Self Report Covid Case")
            print("6: List Covid Notificiation")
            print("7: Exit Program")

            option = input("Enter your Option: ")

            print()
        elif role == "Officer":
            print("Option")
            print("1. Create Covid Case")
            print("2: Exit Program")

            option = input("Enter your Option ")
            print()

        print("Option Selected: " + option)
        print("Current role " + role)

        # Option: Check in 
        if option == "1" and role == "Normal":
            # Select Location
            location = selectLocation()
            if location is None:
                print("Invalid Location")
                loop = False
            else:
                # Check whether check in is individual or group
                print()
                groupcheckin = input("Would like to Group Check in? (y/n) ")
                print()
                if groupcheckin == "y":
                    # Perform Query to Select groups
                    group = selectGroup() 
                    if group is None:
                        print("Invalid Group")
                        loop = False
                    else:
                        # Perform Check-in for Group
                        status = checkInGroup(location.name, group)
                        if status is False:
                            loop = False

                elif groupcheckin == "n":
                    # Perform Check-in for Individual
                    status = checkInIndivudal(location.name)
                    if status is False:
                        loop = False

                else:
                    print("Please Enter a correct option; either y or no")
                    loop = True

        # Option: Check out
        elif option == "2" and role == "Normal":
            status = getCheckOutOptions()
            if status is None:
                print("Invalid Check out option")
                loop = False
            else:
                continue 

        # Option: Create Group
        elif option == "3" and role == "Normal":
            createGroup(group_name=None) 
        
        elif option == "4" and role == "Normal":
            status = getSafeEntryHistory()
            if (status == False):
                print("Error during Self Reporting Operation")
                loop = False

        elif option == "5" and role == "Normal":
            getCovidLocationByUser(name)

        elif option == "6" and role == "Normal":
            print("Notificiation")
            getNotificiationByUser()

        elif option == "1" and role == "Officer":
            print("Select Location that has Covid Cases")
            location = selectLocation()
            createCovidCase(location.id)

        elif (option == "7" and role == "Normal") or (option == "2" and role == "Officer"):
            print("Existing Program")
            loop = False 

        else:
            print("An Error has occured. Please Re-run Program")
            loop = False


# Conidition: Check input is int or str