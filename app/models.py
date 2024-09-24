import mysql.connector
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from flask import flash

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

def create_company(company_name, domain):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Sprawdzanie, czy firma już istnieje
    cursor.execute("SELECT * FROM companies WHERE CompanyDomain = %s", (domain,))
    existing_company = cursor.fetchone()
    
    if existing_company:
        flash(f"Found existing company: {existing_company[1]} with domain {existing_company[2]}")
        flash('Company with this domain already exists.')
        return
        
    
    # Dodawanie nowej firmy
    cursor.execute("INSERT INTO companies (CompanyName, CompanyDomain) VALUES (%s, %s)", (company_name, domain))
    conn.commit()
    
    # Pobieranie ID nowo utworzonej firmy
    company_id = cursor.lastrowid
    
    # Automatyczne tworzenie tabel dla nowej firmy
    cursor.execute(f"""
        CREATE TABLE activities_{company_id} (
            ActivityID INT AUTO_INCREMENT PRIMARY KEY,
            WorkplaceNumber INT,
            OrderName VARCHAR(255),
            PositionName VARCHAR(255),
            ElementNumber INT,
            Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    cursor.execute(f"""
        CREATE TABLE employees_{company_id} (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Status VARCHAR(255),
            First_name VARCHAR(255),
            Last_name VARCHAR(255),
            Job_title VARCHAR(255),
            Line INT
        )
    """)
    
    cursor.execute(f"""
        CREATE TABLE lines_tables_{company_id} (
            LineID INT AUTO_INCREMENT PRIMARY KEY,
            Week INT,
            AvailableManHoursWeek1 FLOAT,
            AvailableManHoursWeek2 FLOAT,
            AvailableManHoursWeek3 FLOAT,
            AvailableManHoursWeek4 FLOAT,
            AvailableManHoursWeek5 FLOAT,
            AvailableManHoursWeek6 FLOAT,
            AvailableManHoursWeek7 FLOAT,
            AvailableManHoursWeek8 FLOAT,
            AvailableManHoursWeek9 FLOAT,
            AvailableManHoursWeek10 FLOAT,
            AvailableManHoursWeek11 FLOAT,
            AvailableManHoursWeek12 FLOAT,
            AvailableManHoursWeek13 FLOAT,
            AvailableManHoursWeek14 FLOAT,
            AvailableManHoursWeek15 FLOAT,
            AvailableManHoursWeek16 FLOAT,
            AvailableManHoursWeek17 FLOAT,
            AvailableManHoursWeek18 FLOAT,
            AvailableManHoursWeek19 FLOAT,
            AvailableManHoursWeek20 FLOAT,
            AvailableManHoursWeek21 FLOAT,
            AvailableManHoursWeek22 FLOAT,
            AvailableManHoursWeek23 FLOAT,
            AvailableManHoursWeek24 FLOAT,
            AvailableManHoursWeek25 FLOAT,
            AvailableManHoursWeek26 FLOAT,
            AvailableManHoursWeek27 FLOAT,
            AvailableManHoursWeek28 FLOAT,
            AvailableManHoursWeek29 FLOAT,
            AvailableManHoursWeek30 FLOAT,
            AvailableManHoursWeek31 FLOAT,
            AvailableManHoursWeek32 FLOAT,
            AvailableManHoursWeek33 FLOAT,
            AvailableManHoursWeek34 FLOAT,
            AvailableManHoursWeek35 FLOAT,
            AvailableManHoursWeek36 FLOAT,
            AvailableManHoursWeek37 FLOAT,
            AvailableManHoursWeek38 FLOAT,
            AvailableManHoursWeek39 FLOAT,
            AvailableManHoursWeek40 FLOAT,
            AvailableManHoursWeek41 FLOAT,
            AvailableManHoursWeek42 FLOAT,
            AvailableManHoursWeek43 FLOAT,
            AvailableManHoursWeek44 FLOAT,
            AvailableManHoursWeek45 FLOAT,
            AvailableManHoursWeek46 FLOAT,
            AvailableManHoursWeek47 FLOAT,
            AvailableManHoursWeek48 FLOAT,
            AvailableManHoursWeek49 FLOAT,
            AvailableManHoursWeek50 FLOAT,
            AvailableManHoursWeek51 FLOAT,
            AvailableManHoursWeek52 FLOAT
        )
    """)

    cursor.execute(f"""
        CREATE TABLE workplaces_{company_id}(
            WorkplaceID INT AUTO_INCREMENT PRIMARY KEY,
            LineID INT,
            CONSTRAINT fk_LineID
                FOREIGN KEY (LineID) REFERENCES lines_table_{company_id}(LineID),
            CurrentScanerUser1 INT,
            CurrentScanerUser2 INT,
            CurrentScanerUser3 INT,
            CurrentScanerUser4 INT,
            CurrentScanerUser5 INT
        )
    """)

    cursor.execute(f"""
        CREATE TABLE production_plan_{company_id} (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Order TEXT,
            State TEXT,
            Offer TEXT,
            Client TEXT,
            Quantity INT,
            Manhours_offer FLOAT,
            Production_line INT,
            Start_production DATE,
            Completion_date DATE,
            Technolog TEXT,
            Comments TEXT,
            Order_date DATE,
            Material DATE,
            Additions DATE,
            Docu DATE,
            Warehouse DATE,
            Saw DATE,
            CNC DATE,
            Clamping DATE,
            Assembling DATE,
            Quality_control DATE,
            Packing DATE
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

    flash('Company and related tables created successfully.')