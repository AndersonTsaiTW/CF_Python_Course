
import os  # import the os module
print(os.getcwd())

print("----- use chdir -----")
os.chdir(r'C:\Users\ander\OneDrive\Documents\GitHub\CF_Python_Course\Exercise01_4')
print(os.getcwd())
print(os.listdir())
# file = open('hello.txt', 'r')
# print(file)

print("----- mkdir and listdir -----")
os.mkdir('aaa_new_folder')
print(os.listdir())
os.rmdir('aaa_new_folder')
print(os.listdir())
