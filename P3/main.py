menuActive = 1

def factorial(number):
    value = 1
    for i in range(1, number+1):
        value *= i
    print(f'\nThe factorial of {str(number)} is {str(value)}\n')

def fibonacci(n):
    a = 0
    b = 1
    c = a+b
    i = 1
    print('\n')
    while(i<=n):
        if i == 1: 
            # 1st and 2nd numbers are always 1
            print(f"1st sequence: 1", )
            i = 2
        print(i, "th sequence: ", c)
        i += 1
        a = b
        b = c
        c = a+b
    print('\n')

while menuActive == 1:
    print('CS 12TH PRACTICAL 3 MENU')
    print('Type \'factorial <value>\' to find factorial of <value>')
    print('Type \'fibonacci <range>\' to find fibonacci till <range>')
    print('Type \'exit\' to exit the menu.')
    response = (input("Input: ")).split(" ")


    if response[0] == "factorial":
        try:
            factorial(int(response[1]))
        except ValueError:
            print(f"{response[1]} is not a Number!")
        except:
            print('Error Occured! Try Again!')
    elif response[0] == "fibonacci":
        try:
            fibonacci(int(response[1]))
        except ValueError:
            print(f'{response[1]} is not a Number!')
    elif response[0] == "exit":
        print("Exiting the Menu...")
        menuActive = 0