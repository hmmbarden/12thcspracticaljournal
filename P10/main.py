import mysql.connector
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    password="admin",
    port="3306",
    database="school"
)

menuActive = 1

cursor = connection.cursor()

def init_database():
    try:
        cursor.execute('create table students(ROLL_NO int, STNAME char(10))')
        connection.commit()
    except:
        return

init_database()

def enter_records():
    name = input("Enter Student Name: ")
    roll_no = int(input("Enter Roll No: "))
    try:
        cursor.execute(f"insert into students (ROLL_NO, STNAME) Values ({roll_no}, '{name}')")
        connection.commit()
        print("Entry added!\n")
    except Exception as e:
        print("Error Occured! Error: ", e)

def display_contents():
    cursor.execute('select * from students')
    data = cursor.fetchall()
    print("\n")
    for i in data:
        print(f'Roll No: {i[0]}, Name: {i[1]}')
    print("\n")


while menuActive == 1:
    print('CS 12TH PRACTICAL 10 MENU')
    print('Type 1 to enter contents')
    print('Type 2 to view database contents')
    print('Type 3 to exit menu')
    try: 
        response = int(input("Enter: "))
        if response == 3:
            print("Exiting menu...")
            menuActive = 0
        elif response == 1:
            enter_records()
        elif response == 2:
            display_contents()

    except ValueError:
        print("Response is not a number!")
