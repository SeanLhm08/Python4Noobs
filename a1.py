import re

# Fill these in with your details
__author__ = "Your Name"
__email__ = "Your Email"
__date__ = "03/03/2023"

from constants import *

# Write your functions here

def is_integer_regex(s):
    for i in s:
       if(re.fullmatch(r"[-+]?\d+",i)) is not None:
           return i







def main():
    """ Write your docstring """
    # cook book
    recipe_collection = [
        CHOCOLATE_PEANUT_BUTTER_SHAKE, 
        BROWNIE, 
        SEITAN, 
        CINNAMON_ROLLS, 
        PEANUT_BUTTER, 
        MUNG_BEAN_OMELETTE
    ]
    
    # Added dummy text for now, when you done with function remove and call function
    while (True):
        command = input("Please enter a command: ").strip().lower()

        if(command == "q"):
            break

        if(command == "h"):
            print(HELP_TEXT)
        elif(command.startswith('add')):
            recipe = command[3:].strip()
            print(recipe)
        elif(command.startswith('rm -i')):
            ingredients = command[5:].strip()
            ingredients_list = ingredients.split()
            (is_integer_regex(ingredients_list))

        elif(command.startswith('rm')):
            recipe = command[2:].strip()
        elif(command == "g"):
            print("Hello")
        elif(command == "ls"):
            print("Hello")
        elif(command == "ls -a"):
            print("hello")
        elif(command == "ls -s"):
            print('hello')
        elif(command == "mkrec"):
            print("hello")
        else:
            print("Wrong command fk")


if __name__ == "__main__":
    main()
