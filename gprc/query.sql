-- Login
SELECT r.rolename FROM Users u 
    INNER JOIN Roles r 
        ON u.role_id = r.id
    WHERE u.name = %s and u.nric = %s;


-- Get SafeEntry By User
SELECT l.name, c.check_in, c.check_out, g.name from Checkinouts c
    INNER JOIN Users u
        ON c.user_id = u.id
    INNER JOIN Locations l 
        ON c.location_id = l.id
    LEFT JOIN Groups g 
        ON c.group_id = g.id
    WHERE u.id = (
        SELECT id from Users 
            WHERE name = 'user1'
    );

-- Create new Checkin 
INSERT INTO Checkinouts (user_id, location_id)
    VALUES (
        (SELECT id FROM Users WHERE name = 'user1'),
        (SELECT id FROM Locations WHERE name = 'Orchard Road')
    );

-- SELECT GROUP
SELECT DISTINCT u.name FROM Users u
    INNER JOIN UserGroups ug 
        ON u.id = ug.user_id 
    INNER JOIN Groups g 
        ON g.id = ug.group_id 
    WHERE g.id = (
        SELECT id FROM Groups 
            WHERE name = 'group1' 
    );

-- Get Latest Check-in By Location
UPDATE Checkinouts c
SET check_out = CURRENT_TIMESTAMP
WHERE c.id = (
    SELECT c.id FROM Checkinouts c
        INNER JOIN Users u
            ON c.user_id = u.id 
        INNER JOIN Locations l 
            ON c.location_id = l.id
        WHERE u.name = 'user1' AND l.name = 'Orchard Road'
        ORDER BY c.check_in DESC
    LIMIT 1
);

-- Get All Location 
SELECT name FROM locations;

-- Get All Groups By User
SELECT g.name FROM Groups g
    INNER JOIN UserGroups ug 
        ON ug.group_id = g.id 
    INNER JOIN Users u  
        ON ug.user_id = u.id 
    WHERE u.name = 'user1';

-- Create Group
INSERT INTO Groups (name) VALUES ('group2') returning id;

-- Add User into Group 
 INSERT INTO UserGroups (user_id, group_id) VALUES (
    (SELECT id FROM Users WHERE name = 'user1'),
    2
);

-- Create Covid Case
INSERT INTO Cases (user_id, location_id) VALUES (
    (SELECT id FROM Users WHERE name = %s),
    (SELECT id FROM Locations WHERE name = %s)
);

-- Get All Users associated with Cases in the past 14 days 
SELECT DISTINCT u.name FROM Users u 
    INNER JOIN Checkinouts c 
        ON u.id = c.user_id
    WHERE c.check_in::DATE - 14 <= (
        SELECT date FROM Cases WHERE id = 2
    );

-- Check User Roles
SELECT r.rolename FROM Roles r 
    INNER JOIN Users u 
        ON u.role_id = r.id 
    WHERE u.name = 'user1';

-- Select Available Check-in Options
SELECT u.name, g.name, l.name from Checkinouts c 
    INNER JOIN Locations l 
        ON l.id = c.location_id
    INNER JOIN Users u 
        ON c.user_id = u.id 
    LEFT JOIN Groups g 
        ON c.group_id = g.id
    WHERE c.check_out IS NULL;

-- Get All user except for added users
SELECT u.name FROM Users u
    INNER JOIN Roles r 
        ON u.role_id = r.id 
    WHERE name NOT IN ('user1') and r.rolename = 'Normal';

-- Get All Locations visited by current user in the past 14 days
SELECT DISTINCT l.name FROM Locations l 
    INNER JOIN Checkinouts c
        ON l.id = c.location_id
    INNER JOIN Users u 
        ON u.id = c.user_id
    WHERE c.check_in::DATE - 14 <= NOW()
        AND u.name = 'user1';