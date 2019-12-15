'Write code about maths, calculator'
import sys
from time import *
check_ok = False


def math_menu():
    for c in "Welcome To Calculator, 1 = Add, 2 = Subtract, 3 = Multiply, 4 = Divide, 5 = Exit":
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.03)
    sys.stdout.write('\n')
    sys.stdout.flush()
    for c in "Please input 1 - 5":
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.04)
    sys.stdout.write(" ")
    sys.stdout.flush()
    while True:
        user_input = input()
        if user_input == "1":
            print("Moving to the add menu\n")
            add()
            check_ok = True
        elif user_input == "2":
            print("Moving to the subtract menu\n")
            subtract()
            check_ok = True
        elif user_input == "3":
            print("Moving to the multiplication menu\n")
            multiply()
            check_ok = True
        elif user_input == "4":
            print("Moving to the divide menu\n")
            divide()
            check_ok = True
        elif user_input == "5":
            print("Exiting\n")
        else:
            print("Please write 1 to 5\n")
            check_ok = False
                    
    

def add():
    for c in "Welcome to the add menu, Please enter two values":
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.03)
    sys.stdout.write('\n')
    sys.stdout.flush()
    add_1 = float(input("First Value - "))
    add_2 = float(input("Second Value - "))
    total = add_1 + add_2
    print("Here is the total - " + str(total))
    while True:
        user_input_2 = input("Do you want to go back to the menu?, y = yes or n = no ")
        if user_input_2 == "y":
            print("Going to back to the main menu\n")
            math_menu()
            check_ok = True
        if user_input_2 == "Y":
            print("Going to back to the main menu\n")
            math_menu()
            check_ok = True
        elif user_input_2 == "n":
            print("Goodbye")
            sys.exit()
            check_ok = True
        elif user_input_2 == "N":
            print("Goodbye")
            sys.exit()
            check_ok = True
        else:
            print("Y or N")
            check_ok = False

def subtract():
    for c in "Welcome to the subtract menu, Please enter two values":
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.03)
    sys.stdout.write('\n')
    sys.stdout.flush()
    subtract_1 = float(input("First Value - "))
    subtract_2 = float(input("Second Value - "))
    total = subtract_1 - subtract_2
    print("Here is the total - " + str(total))
    while True:
        user_input_2 = input("Do you want to go back to the menu?, y = yes or n = no ")
        if user_input_2 == "y":
            print("Going to back to the main menu\n")
            math_menu()
            check_ok = True
        if user_input_2 == "Y":
            print("Going to back to the main menu\n")
            math_menu()
            check_ok = True
        elif user_input_2 == "n":
            print("Goodbye")
            sys.exit()
            check_ok = True
        elif user_input_2 == "N":
            print("Goodbye")
            sys.exit()
            check_ok = True
        else:
            print("Y or N")
            check_ok = False

def multiply():
    for c in "Welcome to the Multiply menu, Please enter two values":
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.03)
    sys.stdout.write('\n')
    sys.stdout.flush()
    multiply_1 = float(input("First Value - "))
    multiply_2 = float(input("Second Value - "))
    total = multiply_1 * multiply_2
    print("Here is the total - " + str(total))
    while True:
        user_input_2 = input("Do you want to go back to the menu?, y = yes or n = no ")
        if user_input_2 == "y":
            print("Going to back to the main menu\n")
            math_menu()
            check_ok = True
        if user_input_2 == "Y":
            print("Going to back to the main menu\n")
            math_menu()
            check_ok = True
        elif user_input_2 == "n":
            print("Goodbye")
            sys.exit()
            check_ok = True
        elif user_input_2 == "N":
            print("Goodbye")
            sys.exit()
            check_ok = True
        else:
            print("Y or N")
            check_ok = False

def divide():
    for c in "Welcome to the divide menu, Please enter two values":
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.03)
    sys.stdout.write('\n')
    sys.stdout.flush()
    divide_1 = float(input("First Value - "))
    divide_2 = float(input("Second Value - "))
    total = divide_1 / divide_2
    print("Here is the total - " + str(total))
    while True:
        user_input_2 = input("Do you want to go back to the menu?, y = yes or n = no ")
        if user_input_2 == "y":
            print("Going to back to the main menu\n")
            math_menu()
            check_ok = True
        if user_input_2 == "Y":
            print("Going to back to the main menu\n")
            math_menu()
            check_ok = True
        elif user_input_2 == "n":
            print("Goodbye")
            sys.exit()
            check_ok = True
        elif user_input_2 == "N":
            print("Goodbye")
            sys.exit()
            check_ok = True
        else:
            print("Y or N")
            check_ok = False
            
    





def main():
    math_menu()

main()
