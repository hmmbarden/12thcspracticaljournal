

string_1 = input("Enter string: ")
string_2 = input("Enter another string: ")
try:
    string = string_1 + string_2
    print(f"Concatenated String: {string}")
except Exception as e:
    print("Error Occured: ", e)

