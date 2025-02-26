def display(file):
    heroes = []
    for line in file:
        # Removing newline characters
        line = line.rstrip("\n")

        # Here, we use the split(", ") method available to strings
        # to split the hero name and the year separately.
        # The separation occurs at ", ".

        # Taking the first element of the split
        hero_name = line.split(", ")[0]
        # Taking the second element of the split
        first_appearance = line.split(", ")[1]

        # We pack these two into a smaller, two-element
        # list, and then append it to the list "heroes".
        heroes.append([hero_name, first_appearance])

    # Now, we'll sort "heroes" by first appearance.
    heroes.sort(key=lambda hero: hero[1])

    for hero in heroes:
        print("--------------------------------------")
        print("Superhero: " + hero[0])
        print("First year of appearance: " + hero[1])


filename = input("Enter the filename where you've stored your superheroes: ")
try:
    file = open(filename, 'r')
    display(file)
except FileNotFoundError:
    print("File doesn't exist - exiting.")
except:
    print("An unexpected error occurred.")
else:
    file.close()
finally:
    print("Goodbye!")


# # 一個將輸入數字加 10 的 lambda 函數
# add_ten = lambda x: x + 10
# print(add_ten(5))  # 輸出：15

# # 一個計算兩個數字乘積的 lambda 函數
# multiply = lambda x, y: x * y
# print(multiply(3, 4))  # 輸出：12
