menuActive = 1

def create_tuple(list):
    return tuple(list)
def findminmax(tuple):
    min = tuple[0]
    max = tuple[-1]
    solution = [min, max]
    return solution
def find_average(tuple):
    # average = (sum)/(element_count)
    element_count = 0
    sum = 0
    for i in range(len(tuple)):
        sum += int(tuple[i])
        element_count += 1
    return float(sum/element_count)

while menuActive == 1:
    print('CS 12TH PRACTICAL 4 MENU')
    print('Type \'make-tuple <list>\' to make a tuple.')
    print('Type \'findminmax <list>\' to find min and max of list defined above.')
    print('Type \'average\' to find average of all numbers in tuple.')
    print('Type\'exit\' to exit the menu.')
    
    response = input('Input: ').split(' ')
    if response[0] == "make-tuple":
        try:
            list = response
            list.pop(0)
            tuple = create_tuple(list)
            print(f"\nGenerated Tuple: {tuple}\n")
        except IndexError:
            print("No List Provided or List is less than 2 elements long!")
    elif response[0] == "findminmax":
        list = response
        list.pop(0)
        solution_list = findminmax(create_tuple(list))
        print(f'\nMinimum Value: {solution_list[0]}, Maximum Value: {solution_list[1]}\n')
    elif response[0] == "average":
            list = response
            list.pop(0)
            print(f"\nThe average of given numbers is {str(find_average(tuple(list)))}\n")
    elif response[0] == "exit":
        print("Exiting the menu...")
        menuActive = 0
