CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    pw_hash VARCHAR(255) NOT NULL);

CREATE TABLE test (
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(255) NOT NULL,
text VARCHAR(255) NOT NULL,
time TIMESTAMP NULL DEFAULT
(((now() + interval 5 hour) + interval 30 minute))
);

CREATE TABLE feedback (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(255),
feedback TEXT,
post_id INT,
time TIMESTAMP NULL DEFAULT
(((now() + interval 5 hour) + interval 30 minute))
);