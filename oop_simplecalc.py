# Redo the Simple Calculator with OOP
from ui_class import UI
from calculator_class import Calculator, ScientificCalculator

def Introduction():
    import time
    print("Welcome to the Calculator!")
    time.sleep(2)

def SimpleCalculator():
    # initializes class
    calculate = Calculator('', '', '')
    userInterface = UI('')
    # takes input from user that determines the type of arithmetic operation to use
    while True:
        user_choice = str(input("\nType the symbol of the arithmetic operation you would like to use\n( + , - , * , / )\n: "))
        if user_choice == '+':
            userInterface.intro_add()
            break
        elif user_choice == '-':
            userInterface.intro_sub()
            break
        elif user_choice == '*':
            userInterface.intro_mul()
            break
        elif user_choice == '/':
            userInterface.intro_div()
            break
        else:
            print("Invalid.")
        return user_choice

    # takes input and stores it into variables
    firstN = float(input("\nWhat is your first number?\n"))
    calculate.inputNum1(firstN)
    secondN = float(input("\nWhat is your second number?\n"))
    calculate.inputNum2(secondN)

    # does the calculations based on the arithmetic operation
    if user_choice == '+':
        calculate.addition()
    elif user_choice == '-':
        calculate.subtraction()
    elif user_choice == '*':
        calculate.multiplication()
    elif user_choice == '/':
        calculate.division()

    # prints out results
    userInterface.animated(firstN, secondN, calculate.results)

def Retry():
    while True:
        again=str(input("\nTry again? (y/n only)\n: "))
        if again=='y':
            SimpleCalculator()
            continue
        elif again=='n':
            break
        else:
            print("Invalid.\n")

# executes the code
try:
    Introduction()
    SimpleCalculator()
    Retry()
except:
    print("\nInvalid.\n")
finally:
    print("\nThank you!")

# HONTIVEROS, JEROME ANDREI O.
# BSCPE 1-5
