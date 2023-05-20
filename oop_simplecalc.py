# Redo the Simple Calculator with OOP
from ui_class import UI
def Animated():
    animated=UI
    animated.start()
    while True:
        user_choice=str(input("\nType the symbol of the arithmetic operation you would like to use\n( + , - , * , / )\n: "))
        if user_choice=='+':
            animated.intro_add()
        elif user_choice=='-':
            animated.intro_sub()
        elif user_choice=='*':
            animated.intro_mul()
        elif user_choice=='/':
            animated.intro_div()
        else:
            print("Invalid.")
Animated()