import psycopg2

def table():
    conn = psycopg2.connect(dbname = "postgres", user="postgres",password="3402",host="localhost",port="5432" )

    cursor =conn.cursor() # cursor is now ready to send SQL commands to the database.
    cursor.execute('''create table employees(Name Text, ID int, Age int);''')
    print("Table create successfully")




    conn.commit()
    conn.close()

def data():
    conn = psycopg2.connect(dbname = "postgres", user="postgres",password="3402",host="localhost",port="5432" )

    cursor =conn.cursor() # cursor is now ready to send SQL commands to the database.
    name = input("Enter name: ")
    id = input("Enter ID: ")
    age = input("Enter age: ")
    query = '''INSERT INTO employees(Name,ID,Age) VALUES(%s,%s,%s);'''
    cursor.execute(query,(name,id,age))
    print("Data added successfully")




    conn.commit()
    conn.close()

data()