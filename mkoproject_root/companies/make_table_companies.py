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
CREATE TABLE companies(
ActivityID INT AUTO_INCREMENT PRIMARY KEY,
CompanyName VARCHAR(255),
CompanyDomain VARCHAR(255)
)
'''

cursor.execute(query)
cursor.close()
connection.close()