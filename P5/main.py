
menuActive = 1
data = {}
def create_dictionary():
    name = input("Name of Student: ").lower()
    marks = int(input(("Marks: ")))
    data[name] = marks
def show_marks(name):
    return data[name]

while menuActive == 1:
    print('CS 12TH PRACTICAL 5 MENU')
    print('Type \'add_entry\' to add to Data')
    print('Type \'show_marks <student_name> \' to get marks of the student.')
    print('Type \'exit\' to exit the menu.')
    response = input("Input: ").split(' ')
    if response[0] == "add_entry":
        print('\n')
        create_dictionary()
        # print data:
        print('Database: \n')
        for i in data:
            print(f'{i}\'s marks: {str(data[i])}')
        print('\n')
    elif response[0] == "show_marks":
        print('\n')
        try:
            print(f'{response[1]}\'s marks are: {data[response[1]]}')
        except:
            print("Enter a correct name!")
        print('\n')
    elif response[0] == "exit":
        print("Exiting the menu..")
        menuActive = 0
