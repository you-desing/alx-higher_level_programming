-- Create MySQL user user_0d_1 with all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user on all databases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
