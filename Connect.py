import pyodbc


class Connect:
    con = pyodbc.connect('Driver={SQL Server};'
                         'Server=SAICHI-SAMA\SQLEXPRESS;'
                         'Database=BasePy;'
                         'Trusted_Connection=yes;')

    cursor = con.cursor()
    cursor.execute('SELECT * FROM Client')


def InsertStaff(self, insertDict):
    con = self.connect
    cur = con.cursor()
    query = f"INSERT INTO Client " \
            f"values ('{insertDict['Id_client']}'," \
            f"'{insertDict['First_name']}'," \
            f"'{insertDict['Second_name']}'," \
            f"'{insertDict['Last_name']}'," \
            f"'{insertDict['Photo_client']}'," \
            f"'{insertDict['Date_of_birth']}'," \
            f"'{insertDict['Email_addres']}'," \
            f"'{insertDict['Date_of_registration']}',"

    try:
        cur.execute(query)
    except pyodbc.Error as err:
        print("Error", err)
        cur.close()

def getStaffAll(self):
        con = self.connect
        cur = con.cursor()
        query = f"SELECT * FROM python"
        try:
            cur.execute(query)
            rows = cur.fetchall()
        except pyodbc.Error as err:
            print("Error", err)
        cur.close()
        return rows

def get_staff_by_surname(self, name):
        con = self.connect
        cur = con.cursor()
        query = f"SELECT * FROM python WHERE first_name='" + name + "'"
        try:
            cur.execute(query)
            rows = cur.fetchall()
        except pyodbc.Error as err:
            print("Error", err)
        cur.close()
        return rows
