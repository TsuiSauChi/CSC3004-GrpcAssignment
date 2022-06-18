import grpc
from concurrent import futures

import tracking_pb2
import tracking_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = tracking_pb2_grpc.TrackingServiceStub(channel)


print("Login into SafeEntry")
Name = input("Input your Name")
NRIC = input("Input your NRIC")


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

       option = input("Enter your Option")

       if option == "1":
           Location = input("Enter Location you would like to check in to")
           Group = input("Would like to Group Check in? (YES/NO)")
           if Group == "YES":
               print()
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

       elif option == "2":
               print()

       elif option == "3":
               print()

       elif option == "4":
               print()
    


