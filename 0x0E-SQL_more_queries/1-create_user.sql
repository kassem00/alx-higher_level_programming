-- Creates DB IF NOT EXISTS  hbtn_0c_0.
-- Creates the user user_0d_1 with all privileges.
CREATE USER
    IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
   ON *.*
   TO 'user_0d_1'@'localhost'
   IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;
