-- Test Case Template for LeetCode 1378: Replace Employee ID With The Unique Identifier
-- Schema and sample data for testing

CREATE TABLE Employees (
    id INT,
    name VARCHAR(100)
);

INSERT INTO Employees (id, name) VALUES
(1, 'Alice'),
(7, 'Bob'),
(11, 'Meir'),
(90, 'Winston'),
(3, 'Jonathan');

CREATE TABLE EmployeeUNI (
    id INT,
    unique_id INT
);

INSERT INTO EmployeeUNI (id, unique_id) VALUES
(3, 1),
(11, 2),
(90, 3);
