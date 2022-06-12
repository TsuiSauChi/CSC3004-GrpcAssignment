INSERT INTO Users (name, nric, phone_number)
    VALUES 
        ('user1', '98765432', '1'),
        ('user2', '98765432', '2'),
        ('user3', '98765432', '3'),
        ('user4', '98765432', '4'),
        ('user5', '98765432', '5'),
        ('user6', '98765432', '6'),
        ('user7', '98765432', '7'),
        ('user8', '98765432', '8'),
        ('user9', '98765432', '9'),
        ('user10', '98765432', '10'),
        ('user11', '98765432', '11');

INSERT INTO Groups (name)
    VALUES 
        ('group1');

INSERT INTO UserGroups (user_id, group_id)
    VALUES 
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 1),
        (6, 1);

INSERT INTO Locations (name)
    VALUES
        ('Orchard Road');

INSERT INTO Buildings (location_id, name, shopping_mall)
    VALUES 
        (1, 'ION Orchard', true),
        (1, 'Far East Plaza', true),
        (1, 'ION Art Gallery', false);

INSERT INTO Stores (building_id, name)
    VALUES 
        (1, 'Jumbo Seafood'),
        (1, 'Toast Box'),
        (2, 'Dunkin Donuts');