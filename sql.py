import sqlite3

## Connect to sqlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Aaditya Adyot','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Shubham Shrivastva','AIML','B',100)''')
cursor.execute('''Insert Into STUDENT values('Shreya','GenAI','A',76)''')
cursor.execute('''Insert Into STUDENT values('Smita','DEVSECOPS','A',55)''')
cursor.execute('''Insert Into STUDENT values('Raju','Java','A',33)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()