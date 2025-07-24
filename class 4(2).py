import mysql.connector
mydb = mysql.connector.connect(
 host='127.0.0.1',
 user='root',
 password='Root123@',
database='employees'
)
print(mydb)
cursor = mydb.cursor()
cursor.execute("DROP TABLE IF EXISTS salary")
sql = """
    CREATE TABLE salary (
        empid INT,
        firstname VARCHAR(100),
        lastname VARCHAR(100),
        email VARCHAR(50),
        phone VARCHAR(15),
        hire_date DATE,
        job_id VARCHAR(15),
        salary INT
) """

cursor = mydb.cursor()
cursor.execute(sql)

import csv
import datetime
filename='D:/python class/AI&ML/employees1.csv'
with open(filename, 'r') as csvfile:
    csvreader =csv.reader(csvfile)
    a = next(csvreader) 
    for row in csvreader: 
        print(row)
        empid = int(row[0])
        firstname = row[1]
        lastname = row[2]
        email = row[3]
        phone = row[4]
        
        hire_date = datetime.datetime.strptime(row[5], '%d-%b-%y').date() 
        job_id = row[6]
        salary = int(row[7])

        sql = """
            INSERT INTO salary (empid, firstname, lastname, email, phone, hire_date, job_id, salary)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
        val = (empid, firstname, lastname, email, phone, hire_date, job_id, salary)
        cursor.execute(sql, val)
        mydb.commit()


mydb.close()