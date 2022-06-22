
CREATE Table Roles (
    id              INTEGER     GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    rolename        TEXT  
);

INSERT INTO Roles (rolename) VALUES ('Normal');
INSERT INTO Roles (rolename) VALUES ('Officer');

CREATE TABLE Users (
    id              INTEGER     GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    role_id         INTEGER     REFERENCES Roles NOT NULL,
    phone_number    TEXT        UNIQUE NOT NULL, 
    nric            TEXT        NOT NULL,
    name            TEXT        NOT NULL
);

CREATE TABLE Groups (
    id              INTEGER     GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name            TEXT        NOT NULL    
);

CREATE TABLE UserGroups (
    user_id         INTEGER     REFERENCES Users,
    group_id        INTEGER     REFERENCES Groups,
    PRIMARY KEY (user_id, group_id)
);

-- To Include Sample Locations, Building, Stores
CREATE TABLE Locations (
    id              INTEGER     GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name            TEXT        UNIQUE NOT NULL
);

CREATE TABLE Buildings (
    id              INTEGER     GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    location_id     INTEGER     REFERENCES Locations,
    name            TEXT        NOT NULL,
    shopping_mall   BOOLEAN
);

CREATE TABLE Stores (
    id              INTEGER     GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY, 
    building_id     INTEGER     REFERENCES Buildings,
    name            TEXT        NOT NULL   
);

CREATE Table Checkinouts (
    id              INTEGER     GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY, 
    user_id         INTEGER     REFERENCES Users,
    group_id        INTEGER     REFERENCES Groups,
    location_id     INTEGER     REFERENCES Locations NOT NULL,
    check_in        timestamptz DEFAULT (CURRENT_TIMESTAMP(0) :: timestamptz),
    check_out       timestamptz
);

CREATE TABLE Cases (
    id              INTEGER     GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    user_id         INTEGER     REFERENCES Users NOT NULL,
    location_id     INTEGER     REFERENCES Locations NOT NULL,
    date            DATE        DEFAULT (CURRENT_TIMESTAMP(0) :: DATE)    
);