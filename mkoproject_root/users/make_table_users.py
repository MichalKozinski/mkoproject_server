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
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(20) NOT NULL
)
'''

cursor.execute(query)
cursor.close()
connection.close()