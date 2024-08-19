from werkzeug.security import generate_password_hash
import mysql.connector

# Konfiguracja bazy danych
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Knf_2291',
    'database': 'mkoproject'
}

# Generowanie hasła
password = 'Knf_2506'  # Zastąp swoim hasłem
hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
print("Hashed Password:", hashed_password)

# Połączenie z bazą danych
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Wstawianie użytkownika admina do bazy danych
try:
    query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
    cursor.execute(query, ('Admin', hashed_password, 'admin'))
    conn.commit()
    print("Admin user added successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    cursor.close()
    conn.close()