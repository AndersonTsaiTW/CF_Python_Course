# Open the file in 'rt' mode (read text mode)
print("--------Open and read files-----------")
my_file = open('./Exercise01_4/desserts.txt', 'rt')

# Read the first 10 characters; the file pointer will move forward
print(my_file.read(10) + "\n")

# Display the current position of the file pointer
print("Now the pointer is at position: " + str(my_file.tell()) + "\n")

# Read the next 10 characters from the current file pointer position
print(my_file.read(10) + "\n")

# Read the rest of the file
string_complete = my_file.read()
print(string_complete + "\n")

# Close the file to release system resources
# my_file.close()

# return to the start and print all
my_file.seek(0)
print(my_file.read() + "\n")

# the readline method
print("--------readline method-----------")
my_file.seek(0)
print(my_file.readline())
print(my_file.readline())

# the readlines method
print("--------readlines method-----------")
my_file.seek(0)
all_desserts = my_file.readlines()
print(all_desserts)
print("\n")

# rstrip: remove the right new line
print("----------rstrip---------")
all_desserts_clean = []
# Methos - 01
all_desserts_clean = [dessert.rstrip('\n') for dessert in all_desserts]
# Method - 02
# for dessert in all_desserts:
#     all_desserts_clean.append(dessert.rstrip('\n'))
print(all_desserts_clean)
print("\n")

# close the file
my_file.close()
