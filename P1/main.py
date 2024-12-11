# WRITE A MENU DRIVEN PROGRAM
# TO PRINT PRIME NUMBERS ACCORDING
# TO THE CHOICE ENTERED BY THE USER

menuActive = 0

def list_primes(minimum, maximum):
    
    if minimum > maximum:
        print("Error Occured! Min value > Max value is unacceptable.")
        return
    elif minimum == maximum:
        print("Error Occured! Min Value = Max Value is unacceptable.")
        return

    number = minimum
    while(number <= maximum):
        factors_count = 0
        # start from min value
        for i in range(1, number+1):
            if (number % i) == 0:
                factors_count += 1
            
        if factors_count == 2:
            print(number, "is a prime.")
        # step in recursive func.
        number += 1

print("Prime Number Program.")
print("With this Program, you can find all\n prime numbers within a certain limit.")
response = input("Enter a Range Limit.\nInput: ").split(" ")

try:
    list_primes(int(response[0]), int(response[1]))
except TypeError:
    print("The Values you've entered aren't Numbers!")
except:
    print("Error occured, please try again!")