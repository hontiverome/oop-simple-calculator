# Redo the Simple Calculator with OOP
from ui_class import UI
from calculator_class import Calculator

def SimpleCalculator():
    calculate=Calculator(1,1)
    userInterface=UI
    userInterface.start()
    while True:
        user_choice=str(input("\nType the symbol of the arithmetic operation you would like to use\n( + , - , * , / )\n: "))
        if user_choice=='+':
            userInterface.intro_add()
            break
        elif user_choice=='-':
            userInterface.intro_sub()
            break
        elif user_choice=='*':
            userInterface.intro_mul()
            break
        elif user_choice=='/':
            userInterface.intro_div()
            break
        else:
            print("Invalid.")
            
    firstN=float(input("\nWhat is your first number?\n"))
    calculate.inputNum1(firstN)
    secondN=float(input("\nWhat is your second number?\n"))
    calculate.inputNum2(secondN)
        
SimpleCalculator()