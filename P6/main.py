
menuActive = 1
def read_lines(char):
    lines = open('P6/lines.txt', 'r').readlines()
    for line in lines:
        string = f"{char}".join(line.split(" "))
        print(string)

while menuActive == 1:
    print("CS 12TH PRACTICAL 6")
    print("Type the char to display sentence where\neach word is sperated by the given char")
    char = input("Input char: ")
    print('\n')
    read_lines(char)
    print('\n')
