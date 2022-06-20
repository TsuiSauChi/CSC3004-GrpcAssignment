
-- Get SafeEntry By User
SELECT * from Checkinouts c
    INNER JOIN Users u
        ON c.user_id = u.id
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