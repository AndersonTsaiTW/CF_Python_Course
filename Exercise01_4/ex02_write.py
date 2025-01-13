my_file = open('./Exercise01_4/hello.txt', 'w')
my_file.write("Hello World!")
my_file.close()

vegetables = ['Tomato\n', 'Carrot\n', 'Cucumber\n']
my_file = open('./Exercise01_4/veggies.txt', 'w')
my_file.writelines(vegetables)
my_file.close()

# with method
print("----- with method will close the file automatically -----")
vegetables = ['Tomato\n', 'Carrot\n', 'Cucumber\n']
with open('./Exercise01_4/veggies.txt', 'w') as my_file:
    my_file.writelines(vegetables)
