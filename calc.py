import sys
menu_ok = False

def menu():
    user_input = input("Welcome to the Z-Calculator!\nPick an option below:\n1) Add numbers\n2) Subtract numbers\n3) Multply numbers\n4) Divide numbers\n5) The power of any number\n6) The root of any number\n7) Exit the code\nPlease select: ")
    while True:
        if user_input == "1":
            print("Moving to the Addition level!\n")
            add()
            menu_ok = True
            break
        elif user_input == "2":
            print("Moving to the Subtraction level\n")
            subtract()
            menu_ok = True
            break
        elif user_input == "3":
            print("Moving to the Multiplication level\n")
            multiply()
            menu_ok = True
            break
        elif user_input == "4":
            print("Moving to the Division level\n")
            divide()
            menu_ok = True
            break
        elif user_input == "5":
            print("Moving to the Power level\n")
            power()
            menu_ok = True
            break
        elif user_input == "6":
            print("Moving to the Root level\n")
            root()
            menu_ok = True
            break
        elif user_input == "7":
            print("Exiting")
            sys.exit()
            menu_ok = True
            break
        else:
            print("\nTry again")
            user_input = input("Enter 1 - 7: ")
            menu_ok = False
        
def menu2():
    print("Would you like to return to the main menu or exit?.")
    while True:
        user_input = input("Press m to go to the menu or e to exit: ")
        if user_input == "m":
            print("\n")
            menu()
            break
        elif user_input == "e":
            sys.exit()
            break
        else:
            print("Try again")
            

def inputNumber(message, num):
  while True:
    try:
        userInput = float(message)
    except ValueError:
       print("Not an integer/decimal! Try again.")
       message = input("New Value {0}: ".format(num))
       message = inputNumber(message, num)
       continue
    else:
       return userInput 
       break 
        
def add():
    print("Please input 2 values you would like to add:")
    a = input("Value 1: ")
    num = "1"
    a = inputNumber(a, num)
    b = input("Value 2: ")
    num = "2"
    b = inputNumber(b, num)
    c = a + b
    print("Here is your answer: {0}".format(c))
    menu2()

def subtract():
    print("Please input 2 values you would like to subtract:")
    a = input("Value 1: ")
    num = "1"
    a = inputNumber(a, num)
    b = input("Value 2: ")
    num = "2"
    b = inputNumber(b, num)
    c = a - b
    print("Here is your answer: {0}".format(c))
    menu2()
    
def multiply():
    print("Please input 2 values you would like to multipliy:")
    a = input("Value 1: ")
    num = "1"
    a = inputNumber(a, num)
    b = input("Value 2: ")
    num = "2"
    b = inputNumber(b, num)
    c = a * b
    print("Here is your answer: {0}".format(c))
    menu2()
    
def divide():
    print("Please input 2 values you would like to divide:")
    a = input("Value 1: ")
    num = "1"
    a = inputNumber(a, num)
    b = input("Value 2: ")
    num = "2"
    b = inputNumber(b, num)
    c = a / b
    print("Here is your answer: {0}".format(c))
    menu2()

    
def power():
    print("Please input 2 values you would like to power:")
    print("Value 1 will be the number to be powered\nValue 2 is the power") 
    a = input("Value 1: ")
    num = "1"
    a = inputNumber(a, num)
    b = input("Value 2: ")
    num = "2"
    b = inputNumber(b, num)
    c = a ** b
    print("Here is your answer: {0}".format(c))
    menu2()
    

def root():
    print("Please input 2 values you would like to root:")
    print("Value 1 will be the number to be rooted\nValue 2 is the root") 
    a = input("Value 1: ")
    num = "1"
    a = inputNumber(a, num)
    b = input("Value 2: ")
    num = "2"
    b = inputNumber(b, num)
    c = a**(1/b)
    print("Here is your answer: {0}".format(c))
    menu2()
    

def main():
    menu()

main()
