import mysql.connector

db_config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : 'Knf_2291',
    'database' : 'mkoproject'
}

connection = mysql.connector.connect(**db_config)

cursor = connection.cursor()
query = '''
CREATE TABLE employees(
EmpID INT AUTO_INCREMENT PRIMARY KEY,
FirstName VARCHAR(255),
LastName VARCHAR(255),
StartDate DATE,
ExitDate DATE,
Title VARCHAR(255),
Supervisor VARCHAR(255),
ADEmail VARCHAR(255),
EmployeeStatus VARCHAR(255),
EmployeeType VARCHAR(255),
PayZone VARCHAR(255),
EmployeeClassificationType VARCHAR(255),
TerminationType VARCHAR(255),
TerminationDescription VARCHAR(255),
DepartmentType VARCHAR(255),
Division VARCHAR(255),
DOB DATE,
State VARCHAR(255),
JobFunctionDescription VARCHAR(255),
GenderCode VARCHAR(255),
LocationCode INT,
RaceDesc VARCHAR(255),
MaritalDesc VARCHAR(255),
PerformanceScore VARCHAR(255),
CurrentEmployeeRating INT
)
'''

cursor.execute(query)
cursor.close()
connection.close()