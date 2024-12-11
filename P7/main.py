
menuActive = 1

vowel_count = 0
lowercase_count = 0
uppercase_count = 0
consonant_count = 0

def count():

    global vowel_count
    global consonant_count
    global lowercase_count
    global uppercase_count

    vowels = ["a", "e", "i", "o", "u"]
    lines = open('P7/lines.txt', 'r').readlines()
    for line in lines:
        for char in line:
            if char.isalpha() and char.lower() in vowels:
                vowel_count += 1
            elif char.isalpha() and char.lower() not in vowels:
                consonant_count += 1

            if char.isalpha() and char.isupper():
                uppercase_count += 1
            elif char.isalpha() and char.islower():
                lowercase_count += 1 

count()


while menuActive == 1:
    print('CS 12TH PRACTICAL 7 MENU')
    print('Type \'check-vowel\' to get vowel count.')
    print('Type \'check-consonant\' to get consonant count.')
    print('Type \'check-upper\' to get uppercase letters count.')
    print('Type \'check-lower\' to get lowercase letters count.')
    print('Type \'exit\' to exit menu.')
    response = input("Input: ")

    if response == "check-vowel":
        print(f"\nThe file has {vowel_count} vowels\n")
    elif response == "check-consonant":
        print(f"\nThe file has {consonant_count} consonants.\n")
    elif response == "check-upper":
        print(f"\n The file has {uppercase_count} uppercase letters.\n")
    elif response == "check-lower":
        print(f"\n The file has {lowercase_count} lowercase letters.\n")
    elif response == "exit":
        print("Exiting the menu..")
        menuActive = 0
