import mysql.connector
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    password="admin",
    port="3306",
    database="customers"
)
cursor = connection.cursor()

def init_database():
    try:
        cursor.execute('create table information(ID char(4), NAME char(10), CITY char(10), BILL_AMOUNT float)')
        connection.commit()
    except:
        return

init_database()

def add_details():
    id = int(input("Enter ID: "))
    name = (input("Enter Customer Name: "))
    city = (input("Enter City Name: "))
    bill_amount = float(input("Enter Billed Amount: "))
    try:
        cursor.execute(f"insert into information(ID, NAME, CITY, BILL_AMOUNT) values ({id}, '{name}', '{city}', {bill_amount})")
        connection.commit()
    except Exception as e:
        print('Error Occured! Error: ', e)

def update_details():
    customer_id = int(input("Enter the ID: "))
    name = input('Enter new name: ')
    city = input('Enter new city: ')
    bill_amount = float(input("Enter new bill amount: "))
    try:
        cursor.execute(f"insert into information( NAME, CITY, BILL_AMOUNT) values ('{name}', '{city}', {bill_amount}) where ID={customer_id}")
        print("Customer Information Updated!")
        connection.commit()
    except Exception as e:
        print('Error Occured! Error: ', e)

def delete_details():
    customer_id = int(input("Enter ID to delete: "))
    try:
        cursor.execute(f'delete from information where ID={customer_id}')
        print("Customer Information Deleted!")
        connection.commit()
    except Exception as e:
        print('Error Occured! Error: ', e)

def display_details():
    cursor.execute('select * from information')
    data = cursor.fetchall()
    print("\nData:")
    print("ID   NAME   CITY   BILL_AMOUNT")
    for i in data:
        print(f"{i[0]}   {i[1]}   {i[2]}   {i[3]}")

menuActive = 1
while menuActive == 1:
    print('CS 12TH PRACTICAL 11 MENU')
    print('Type 1 to add details')
    print('Type 2 to update details')
    print('Type 3 to delete details')
    print('Type 4 to display details')
    print('Type 5 to exit menu')
    try: 
        response = int(input("Response: "))
        print('\n')
        if response == 1:
            add_details()
        elif response == 2:
            update_details()
        elif response == 3:
            delete_details()
        elif response == 4:
            display_details()
        elif response == 5:
            print("Exiting Menu...")
            menuActive = 0
    except ValueError:
        print('Response is not a number!')

