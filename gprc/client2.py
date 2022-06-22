import grpc
from concurrent import futures

import tracking_pb2
import tracking_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = tracking_pb2_grpc.TrackingServiceStub(channel)

print("Weclome to SafeEntry")

print()
print("Login")

# name = input("Enter your Name: ")
# nric = input("Enter your NRIC: ")
#name = 'officer'
name = 'user1'
nric = '98765432'
role = None
location = None

loop = True
option = None

def login(name, nric):
    auth = stub.Login(tracking_pb2.User(name=name,nric=nric))
    if auth.status.status == "F":
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
    print("Listing All Location")
    locations_list = list(stub.GetAllLocations(tracking_pb2.Empty()))
    for count, location in enumerate(locations_list):
        print(str(count+1) + " " + location.name)
    print()
    # User Input for location
    print("Enter Location Option you would like to check in to ")
    i = input("Select Option 1 to " + str(len(locations_list)) + ": ")
    if int(i) > len(locations_list):
        return None 
    else:
        print()
        print("Selected Location: " + locations_list[int(i)-1].name)
        return locations_list[int(i)-1].name

def checkInIndivudal(location):
    result = stub.CreateCheckInIndividual(tracking_pb2.Location(
        name = location
    ))
    if result.status is False:
        print("Individual Check in Failed")
        return False
    else:
        print("Individual Checked in succesfully to " + location)
        return True

def checkInGroup(location, group):
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
    groups_list = list(stub.GetGroupsByUser(tracking_pb2.Empty()))
    print()
    print("Listing Groups")
    for count, group in enumerate(groups_list):
        print(str(count+1) + ": " + group.name)
    print()
    print("Enter a group you would like in check in to")
    i = input("Select Option 1 to " + str(len(groups_list)) + ": ")
    if int(i) > len(groups_list):
        return None 
    else:
        print()
        print("Selected Group: " + groups_list[int(i)-1].name)
        return groups_list[int(i)-1].name

def getCheckOutOptions():
    checkout_list = list(stub.GetCheckOutOptions(tracking_pb2.Empty()))
    print()
    print("Listing Check Out Options")
    for count, check_out in enumerate(checkout_list):
        if (check_out.group.name):
            print(str(count+1) + ": Group " + check_out.group.name + "; Location = " + check_out.location.name)
        else:
            print(str(count+1) + ": Indivudal Check in;  " + " Location = "  + check_out.location.name)
    print()
    print("Enter a option to check out to")
    i = input("Select Option 1 to " + str(len(checkout_list)) + ": ")
    if int(i) > len(checkout_list):
        return None
    else:
        print()
        print("Selected Check out Option: " + i)
        return checkout_list[int(i)-1].id

def checkOut(id):
    result = stub.CreateCheckOut(tracking_pb2.CheckOut(id=id))
    if result.status is False:
        print("Check out Failed")
        return False
    else:
        print("Group out succesful")
        return True

# Come back here
def createGroup(group_name):
    print()
    group_name = input("Enter the new group name: ")
    print("Enetered group name", group_name)
    result = stub.CreateGroup(tracking_pb2.Group(name=group_name))
    if(result.status.status):
        pass
    else:
        createGroup(group_name)

role = login(name, nric)

while loop: 
    print()
    print("##########")

    # Options depending on user roles
    if role == "Normal":
        print("Options")
        print("1: Check in ")
        print("2: Check Out")
        print("3: Create Group")
        print("4: List SafeEntry")
        print("5: Self Report Covid Case")
        print("6: Exit Program")

        option = input("Enter your Option ")

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
                    status = checkInGroup(location, group)
                    if status is False:
                        loop = False

            elif groupcheckin == "n":
                # Perform Check-in for Individual
                status = checkInIndivudal(location)
                if status is False:
                    loop = False

            else:
                print("Please Enter a correct option; either y or no")
                loop = True

    # Option: Check out
    elif option == "2" and role == "Normal":
        check_out_id = getCheckOutOptions()
        if check_out_id is None:
            print("Invalid Check out Option")
            loop = False
        else:
            print("Check out option::: ", check_out_id)
            status = checkOut(check_out_id)

    # Option: Create Group
    elif option == "3" and role == "Normal":
        createGroup(group_name=None) 
    
    elif option == "4" and role == "Normal":
        pass

    elif option == "5" and role == "Normal":
        pass

    elif option == "1" and role == "Officer":
        print("Option 1 Selected")
        pass 

    elif (option == "6" and role == "Normal") or (option == "2" and role == "Officer"):
        print("Exiting Program")
        loop = False 

    else:
        print("An Error has occured. Please Re-run Program")
        loop = False


        