"""

CREATE TABLE Employee (
    EmpID int,
    LastName varchar(255),
    FirstName varchar(255),
    Department varchar(255),
    Salary int
);


select * from Employee;

INSERT INTO Employee VALUES (1, 'Kumar', 'Ashish', 'Dev',1000); 
INSERT INTO Employee VALUES (2, 'Singh', 'Amit', 'tester',2000); 
INSERT INTO Employee VALUES (3, 'Kumar', 'Aman', 'Manager',3000); 
INSERT INTO Employee VALUES (4, 'Kumar', 'Bhaskar', 'Dev',4000); 
INSERT INTO Employee VALUES (5, 'Kumar', 'Tejas', 'HR',5000);

"""

import pyodbc
server = 'LAPTOP-3BTUC69B'
database = 'master'
username = "LAPTOP-3BTUC69B\\Ashish"
password = 'Miilee12#' 
driver= '{ODBC Driver 17 for SQL Server}'



cnxn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};"
                      "Server=LAPTOP-3BTUC69B;"
                      "Database=master;"
                      "Trusted_Connection=yes;")

"""
with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Employee")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone() 
            
"""