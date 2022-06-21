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
    result = stub.CreateCheckInIndividual(tracking_pb2.CheckInIndividual(
        location = location
    ))
    if result.status is False:
        print("Check in Failed")
        return False
    else:
        print("Checked in succesfully to " + location)
        return True

def selectGroup():
    groups_list = list(stub.GetGroupsByUser(tracking_pb2.Empty()))
    print()
    print("Listing Groups")
    for count, group in enumerate(groups_list):
        print(str(count+1) + ": " + group.name)
    print()

role = login(name, nric)

while loop: 
    print()
    print()

    # Options depending on user roles
    if role == "Normal":
        print("Options")
        print("1: Check in ")
        print("2: Check Out")
        print("3: List SafeEntry")
        print("4: Self Report Covid Case")
        print("5: Exit Program")

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

    if option == "1" and role == "Normal":
        # Select Location
        location = selectLocation()
        if location is None:
            print("Invalid Location")
            loop = False
        else:
            # Check whether check in is individual or group
            group = input("Would like to Group Check in? (YES/NO) ")
            if group == "YES":
                # Perform Query to List all groups
                selectGroup() 
                ## Continue Here

            else:
                # Perform Check-in for Individual
                status = checkInIndivudal(location)
                if status is False:
                    loop = False
    elif option == "2" and role == "Normal":
        pass  

    elif option == "3" and role == "Normal":
        pass 
    
    elif option == "4" and role == "Normal":
        pass

    elif option == "1" and role == "Officer":
        print("Option 1 Selected")
        pass 

    elif (option == "5" and role == "Normal") or (option == "2" and role == "Officer"):
        print("Exiting Program")
        loop = False 

    else:
        print("An Error has occured. Please Re-run Program")
        loop = False


        