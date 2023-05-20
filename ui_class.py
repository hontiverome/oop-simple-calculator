# UI class
# creates class
class UI:
    def __init__(self) -> None:
        print("Welcome to the Calculator!")
        
    def start(self, user_choice):
        while True:
            user_choice = str(input("\nType the symbol of the arithmetic operation you would like to use\n( + , - , * , / )\n: "))
            if user_choice == '+':
                print("\nYou chose addition")
                operation='Addition'
            elif user_choice == '-':
                print("\nYou chose subtraction")
                operation='Subtraction'
            elif user_choice == '*':
                print("\nYou chose multiplication")
                operation='Multiplication'
            elif user_choice == '/':
                print("\nYou chose division")
                operation='Division'
            else:
                print("Invalid.\n")
                continue
            return operation
    