INSERT INTO Users (name, nric, phone_number, role_id)
    VALUES 
        ('user1', '98765432', '1', 1),
        ('user2', '98765432', '2', 1),
        ('user3', '98765432', '3', 1),
        ('user4', '98765432', '4', 1),
        ('user5', '98765432', '5', 1),
        ('user6', '98765432', '6', 1),
        ('user7', '98765432', '7', 1),
        ('user8', '98765432', '8', 1),
        ('user9', '98765432', '9', 1),
        ('user10', '98765432', '10', 1),
        ('officer', '98765432', '11', 2);

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
        ('Orchard Road'),
        ('Paya Lebar'),
        ('Parkway Parade'),
        ('Bugis');

INSERT INTO Checkinouts (user_id, location_id, check_in, check_out)
    VALUES 
        (1, 1, '2022-04-19 10:00:00', '2022-04-19 12:00:00'),
        (1, 1, '2022-04-20 10:00:00', '2022-04-20 12:00:00'),
        (1, 1, '2022-04-21 10:00:00', '2022-04-21 12:00:00'),
        (2, 1, '2022-04-22 10:00:00', '2022-04-22 12:00:00'),
        (2, 1, '2022-04-23 10:00:00', '2022-04-23 12:00:00'),
        (2, 1, '2022-04-24 10:00:00', '2022-04-24 12:00:00');