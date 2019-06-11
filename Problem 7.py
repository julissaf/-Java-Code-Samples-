#Julissa Franco
#04/16/2019

# Program solution for Module 2 Problem 7

try:
    with open('file.log') as file:
        read_data =file.read()
except FileNotFoundError:
    print("File not found")
