# UI class
# creates class
class UI():
    # initializes variables
    def __init__(self, operation) -> None:
        self.arithmetic_operation=operation
      
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

    def animated(self, number1,number2, result):
        import time
        print('\nOperation')
        time.sleep(1)
        print(f': {self.arithmetic_operation}')
        time.sleep(1.5)
        print(f"Numbers to be computed")
        time.sleep(1)
        print(f': {number1, number2}\n')
        animation = '...'
        for i in range(len(animation)):
            print(animation[i], end='', flush=True)
            time.sleep(1.5)
        # Print the Result
        print(f"\n\nHere is your result\n:{result}")

# HONTIVEROS, JEROME ANDREI O.
# BSCPE 1-5