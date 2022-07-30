from re import A, T
import psycopg2

# Create a connection to the database
try:
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=123success")
except psycopg2.Error as e:
    print("Error: Could not make a connection to the postgres database")
    print(e)

# the cursor enable the user to execute queries
try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get cursor to the database")
    print(e)

# Help to set automatic commit
conn.set_session(autocommit=True)

# Create a database
try:
    cur.execute("create database myfirstdb")
except psycopg2.Error as e:
    print(e)

# type \l (backlash l) on your psql terminal to check if the database was created successfully.

# close the default postgre database and open our new database called myfirstdb

try:
    conn.close()
except psycopg2.Error as e:
    print(e)

try:
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=myfirstdb user=postgres password=123success")
except psycopg2.Error as e:
    print("Error: Could not make a connection to the postgres database")
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get cursor to the database")
    print(e)


conn.set_session(autocommit=True)

# Create a table on the myfirstdb database
try:
    cur.execute("CREATE TABLE IF NOT EXISTS students (student_id int, name varchar, age int, gender varchar, subject varchar, marks int);")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)
# type \c myfirstdb on your psql terminal to connect to the new database
# to see the created table type "\dt" on your psql terminal

# Inserts two rows on our table

try:
    cur.execute("INSERT INTO students(student_id, name, age, gender, subject, marks) VALUES(%s, %s, %s, %s, %s, %s)",
                (1, "kingsley", 32, "Male", "Python", 96))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO students(student_id, name, age, gender, subject, marks) VALUES(%s, %s, %s, %s, %s, %s)",
                (1, "Gerry", 24, "Female", "Data Engineering", 87))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

# close the connection and cursor

cur.close()
conn.close()
