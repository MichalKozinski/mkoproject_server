import mysql.connector
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Knf_2291',
        database='mkoproject'
    )

def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        return User(user['id'], user['username'], user['password'], user['role'])
    return None

def get_user_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        print(f"User found: {user['username']}")
        print(f"Stored password hash: {user['password']}")
        return User(user['id'], user['username'], user['password'], user['role'])
    return None

def add_user(username, password, role):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                   (username, password, role))
    conn.commit()
    cursor.close()
    conn.close()

def create_initial_admin():
    if not get_user_by_username('admin'):
        hashed_password = generate_password_hash('adminpassword', method='sha256')
        add_user('admin', hashed_password, 'admin')