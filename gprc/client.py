import grpc
from concurrent import futures

import tracking_pb2
import tracking_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = tracking_pb2_grpc.TrackingServiceStub(channel)


print("Login into SafeEntry")
Name = input("Input your Name ")
#98765432
NRIC = input("Input your NRIC ")


validation = stub.Login(tracking_pb2.User(name=Name,nric=NRIC))
print(validation)
if validation.message == "F":
    print("User does not exists")
else:
    # Might want to get User name here
    print("Succesfully Login")
    loop = True
    while loop:
       print("SafeEntry")
       print("Options")
       print("1: Check in ")
       print("2: Check Out")
       print("3: List SafeEntry")
       print("4: Self Report Case")

       option = input("Enter your Option ")

       # 1: Check in
       if option == "1":
           Location = input("Enter Location you would like to check in to ")
           Group = input("Would like to Group Check in? (YES/NO) ")
           if Group == "YES":
                groups = stub.GetGroupsByUser(tracking_pb2.Empty())
                if groups is None:
                    print("User not in any Group")
                    creategroup = input("Would you like to create a group? ")
                    if creategroup == "Yes":
                        groupname = input("Enter group name: ")
                        successCreategroup = stub.CreateGroup(tracking_pb2.Group(name=groupname))
                        print(successCreategroup)
                        if successCreategroup.message == "T":
                            print("Group Created")
                        else:
                            print("Error creating group")
                    else:
                        checkIndividual = input("Would like to check in individually? ")
                        if checkIndividual == "Yes":
                            row = stub.CreateCheckInIndividual(tracking_pb2.CheckInIndividual(location=Location))
                            print(row)
                for group in groups:
                     print("Groups:" + group.name )
                response = input("Select the group you would like to check in with: ")
                successCheckInGroup = stub.CreateCheckInGroup(tracking_pb2.CheckInGroup(name=response,location=Location))
                print(successCheckInGroup)
                if successCheckInGroup.message == "T":
                    print("Group Check In Successfully!")
                else:
                    print("Error")
           elif Group == "NO":
               # CHECK IN CODE HERE FOR INDIVIDUAL
               result = stub.CreateCheckInIndividual(tracking_pb2.CheckInIndividual(
                location = Location
               ))
               print(result)
               if result.message == "F":
                   print("Please try again")
               else:
                   print("You have check in SuccessFully")
       # 2: Check Out
       # Conidition: Need group name and location
       elif option == "2":
               Groupcheckout = input("Would you like to group check out (YES/NO) ")
               if Groupcheckout == "YES":
                   Succesgroupcheckout = stub.CreateCheckOutGroup(tracking_pb2.CheckInGroup(name="group1", location="Orchard Road"))
               else:
                   successIndividualCheckout = stub.CreateCheckOutIndividual(tracking_pb2.CheckInIndividual(location="Orchard Road"))
       # 3: List SafeEntry
       elif option == "3":
               ListEntry = stub.GetSafeEntry(tracking_pb2.Empty())
               for row in ListEntry:
                   print(row)

       # 4: Self Report Case
       elif option == "4":
               print("Self Report Covid Cases ")
               locationcase = input("Please input location of affected:")
               createselfreportcovidcase = stub.CreateReportCovidCase(tracking_pb2.Case(location=locationcase))
               if createselfreportcovidcase.message =="T":
                   print("Case created and nearby people will be notified")
               else:
                   print("Error")

              
    


