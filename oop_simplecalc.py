# Redo the Simple Calculator with OOP
from ui_class import UI
from calculator_class import Calculator

def SimpleCalculator():
    calculate=Calculator
    ui=UI
    ui.start()
    while True:
        user_choice=str(input("\nType the symbol of the arithmetic operation you would like to use\n( + , - , * , / )\n: "))
        if user_choice=='+':
            ui.intro_add()
        elif user_choice=='-':
            ui.intro_sub()
        elif user_choice=='*':
            ui.intro_mul()
        elif user_choice=='/':
            ui.intro_div()
        else:
            print("Invalid.")
            
SimpleCalculator()