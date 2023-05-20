# UI class
# creates class
class UI:
    def __init__(self, operation) -> None:
        self.arithmetic_operation=operation
        
    def start():
        print("Welcome to the Calculator!")

    def intro_add(self):
        print("\nYou chose addition")
        operation = str('Addition')
        self.arithmetic_operation = operation

    def intro_sub(self):
        print("\nYou chose subtraction")
        operation = str('Subtraction')
        self.arithmetic_operation = operation

    def intro_mul(self):
        print("\nYou chose multiplication")
        operation = str('Multiplication')
        self.arithmetic_operation = operation

    def intro_div(self):
        print("\nYou chose division")
        operation = str('Division')
        self.arithmetic_operation = operation 

    def animated(self):
        from calculator_class import Calculator
        import time
        print('\nOperation')
        time.sleep(1)
        print(f': {self.arithmetic_operation}')
        time.sleep(1.5)
        print(f"Numbers to be computed")
        time.sleep(1)
        print(f': {self.number1, self.number2}')
        animation = '...'
        for i in range(len(animation)):
            print(animation[i], end='', flush=True)
            time.sleep(1.5)
        # Print the Result
        print(f"\n\nHere is your result\n:{self.results}")
