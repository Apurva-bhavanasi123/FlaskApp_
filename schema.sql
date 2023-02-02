DROP TABLE IF EXISTS users;

CREATE TABLE users (
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    time_created  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    fname TEXT ,
    lname TEXT,
    
    email TEXT
);
