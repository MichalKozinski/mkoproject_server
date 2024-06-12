import csv
import mysql.connector


CSV_E_FILENAME = 'fixed_employees_data.csv'


def load_csv_file(csv_filename):
    with open(csv_filename, 'r', newline='') as content:
        reader = csv.reader(content)
        data = list(reader)
    return data


def get_conn():
    db_config = {
        'host' : 'localhost',
        'user' : 'root',
        'password' : 'Knf_2291',
        'database' : 'mkoproject'
    }
    return mysql.connector.connect(**db_config)


def process_date(date_str):
    if date_str == '':
        return '0000-00-00'  # lub '0000-00-00' jeśli wolisz użyć daty domyślnej
    return date_str


def fill_emp_tab(conn,data):
    cursor=conn.cursor()
    for row in data:
        cursor.execute(''' INSERT INTO employees (EmpID, FirstName, LastName, StartDate, ExitDate, Title, Supervisor, ADEmail, EmployeeStatus, EmployeeType, PayZone, EmployeeClassificationType, TerminationType, TerminationDescription, DepartmentType, Division, DOB, State, JobFunctionDescription, GenderCode, LocationCode, RaceDesc, MaritalDesc, PerformanceScore, CurrentEmployeeRating)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (row[0], row[1], row[2], process_date(row[3]), process_date(row[4]), row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], process_date(row[16]), row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24]))
        conn.commit()
    # cursor.execute(''' INSERT INTO lines_table  (LineID) VALUES (1)''')
    # cursor.execute(''' INSERT INTO lines_table  (LineID) VALUES (2)''')
    # cursor.execute(''' INSERT INTO lines_table  (LineID) VALUES (3)''')
    # cursor.execute(''' INSERT INTO lines_table  (LineID) VALUES (4)''')
    # cursor.execute(''' INSERT INTO lines_table  (LineID) VALUES (5)''')
    cursor.close()


# def fill_workplaces_tab(conn,data):
#     cursor=conn.cursor()
#     try:
#         for row in data:
#             print(row[0])
#             cursor.execute(''' INSERT INTO workplaces (WorkplaceID ,LineID, CurrentScanerUser1, CurrentScanerUser2, CurrentScanerUser3, CurrentScanerUser4, CurrentScanerUser5 ) VALUES (%s, %s, %s, %s, %s, %s, %s)''', (int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6])))
#             conn.commit()
#     except Exception as e:
#             print(e)
#     finally:
#         cursor.close()


def main():
    data_emp=load_csv_file(CSV_E_FILENAME)
    conn=get_conn()
    if conn:
        print('ok')
    else:
        print('blad')
    fill_emp_tab(conn,data_emp)
    conn.close()


if __name__ == '__main__':
    main()