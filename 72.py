filename = input("Enter the file name: ")
line_to_append = input("Enter the line to append: ")

with open(filename, 'a') as file:
    file.write(line_to_append + '\n')

