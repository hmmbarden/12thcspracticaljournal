import random # for option (b)

menuActive = 1

def palindrome(string):
    length  = len(string)
    for i in range(int(length/2)):
        if string[i] == string[-i-1]:
            continue
        else:
            print(f'\nthe string {string} is not a palindrome!\n')
            return
    print(f'\nThe string {string} is a palindrome!\n')

while (menuActive == 1):
    print('CS 12TH PRACTICAL 2 MENU:')
    print('Type \'palindrome\' to check if a string is palindrome.')
    print('Type \'rolldice\' to roll a dice.')
    response = input("Input: ")
    if response == "palindrome":
        word = input("Type a word: ")
        palindrome(word)
    elif response == "rolldice":
        print("You rolled a ", random.randint(1,6), ".\n")