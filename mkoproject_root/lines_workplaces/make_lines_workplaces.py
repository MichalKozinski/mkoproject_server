import mysql.connector


def get_conn():
    db_config = {
        'host' : 'localhost',
        'user' : 'root',
        'password' : 'Knf_2291',
        'database' : 'mkoproject'
    }

    return mysql.connector.connect(**db_config)

def make_table_lines(conn):
    cursor=conn.cursor()
    query = '''
    CREATE TABLE lines_table(
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
    '''
    cursor.execute(query)
    cursor.close()

def make_table_workplaces(conn):
    cursor=conn.cursor()
    query = '''
    CREATE TABLE workplaces(
    WorkplaceID INT AUTO_INCREMENT PRIMARY KEY,
    LineID INT,
    CONSTRAINT fk_LineID
        FOREIGN KEY (LineID) REFERENCES lines_table(LineID),
    CurrentScanerUser1 INT,
    CurrentScanerUser2 INT,
    CurrentScanerUser3 INT,
    CurrentScanerUser4 INT,
    CurrentScanerUser5 INT
    )
    '''
    cursor.execute(query)
    cursor.close()

def main():
    conn = get_conn()
    make_table_lines(conn)
    #make_table_workplaces(conn)
    conn.close()
        


if __name__ == '__main__':
    main()