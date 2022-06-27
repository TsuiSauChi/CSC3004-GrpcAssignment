# CSC3004-GrpcAssignment

## gRPC Python 

Navigate to the gRPC directory
```console
cd ./grpc
```

### Installing Dependencies 

The requirement dependencies can be found in ./grpc/requirement.txt 

Install dependencies using the following command

```console
pip install -r requirements.txt
```

### Program 
The gRPC server can be found in ./grpc/server.py

Run the Server 
```console
python server.py
```

The gRPC client can be found in ./grpc/client.py 

Run the Client
```console
python client.py
```

User are required to login to use the features The following login credentials are provided 

The user and officer are pre-set in the system

| Normal User | |
| :---: | :---: |
| name: | user1 (The following name works as well: user1,user2,user3,... user10) |
| nric: | 98765432 |


| Officer | |
| :---: | :---: |
| name: | officer | 
| nric: | 98765432 |

### Program Workflow 
[Link](https://lucid.app/lucidchart/b1c7c468-21b4-4b1b-b99d-e1d551b86356/edit?beaconFlowId=09A56F5E27E61C07&invitationId=inv_969932a0-885a-4c27-bd9d-d11481b230ae&page=.Rap7O6oXTEJ#)

### Program Flow 

After Login, user will be prompted serveral options 

![image](https://user-images.githubusercontent.com/23652958/175937341-6ee6b943-ba7a-4011-874f-c96d3297dd72.png)

Users will be able to naviagte the UI by selecting the available options

If an invalid input is selected, users are required to re-run the client program

![image](https://user-images.githubusercontent.com/23652958/175937612-fbcf28c0-dee8-4e96-bcfd-389d234f8b08.png)

## Database (PostgreSQL)

### ER Diagram
[Link](https://lucid.app/lucidchart/b1c7c468-21b4-4b1b-b99d-e1d551b86356/edit?beaconFlowId=09A56F5E27E61C07&invitationId=inv_ef2c0d13-e75d-4aa1-9898-cd7c4afb5faa&page=0_0#)

### Installation 

Accessing the database would require 'psql' to be installed

The installation guide can be found in [postgresql_guide.pdf](https://github.com/TsuiSauChi/CSC3004-GrpcAssignment/blob/main/postgresql_guide.pdf)

### Connection

```console
psql -d testing -U postgres -h 174.138.23.75 -p 5432
```

Password: cl0udplus!

### Script 

Navigate to the Database Directory

```console
cd Database
```

Drop Schema 
```console
psql -d testing -U postgres -h 174.138.23.75 -p 5432 -f './drop.sql'
```

Create Schema 
```console
psql -d testing -U postgres -h 174.138.23.75 -p 5432 -f './main.sql'
```

Bootstrap with Sample Data
```console
psql -d testing -U postgres -h 174.138.23.75 -p 5432 -f './init.sql'
```

