import mysql.connector
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

def get_db():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Knf_2291',
        database='mkoproject'
    )
    return connection

class User(UserMixin):
    def __init__(self, id, username, password_hash, role):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.role = role

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

def get_user_by_id(user_id):
    connection = get_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    cursor.close()
    connection.close()
    if user_data:
        return User(user_data['id'], user_data['username'], user_data['password_hash'], user_data['role'])
    return None

def get_user_by_username(username):
    connection = get_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user_data = cursor.fetchone()
    cursor.close()
    connection.close()
    if user_data:
        return User(user_data['id'], user_data['username'], user_data['password_hash'], user_data['role'])
    return None

def add_user(username, password, role):
    connection = get_db()
    cursor = connection.cursor()
    user = User(None, username, None, role)
    user.set_password(password)
    cursor.execute(
        "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)",
        (user.username, user.password_hash, user.role)
    )
    connection.commit()
    cursor.close()
    connection.close()