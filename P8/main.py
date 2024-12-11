

menuActive = 1
def migrate_lines(char):
    file_1_read = open('P8/file_1.txt', 'r')
    file_2_write = open('P8/file_2.txt', 'w')
    lines = file_1_read.readlines()
    for line in lines:
        if char in line:
            lines.remove(line)
            file_2_write.write(line)
    file_1_write = open('P8/file_1.txt', 'w')
    for i in lines:
        file_1_write.write(i)
while menuActive == 1:
    print('\n')
    print('CS 12TH PRACTICAL 8 MENU')
    response = input('Type character: ')
    migrate_lines(response)

