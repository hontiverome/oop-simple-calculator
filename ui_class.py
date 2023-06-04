# UI class
# creates class
class UI():
    # initializes variables
    def __init__(self, operation) -> None:
        self.arithmetic_operation=operation
    
    # registers addition unto variable operation
    def intro_add(self):
        print("\nYou chose addition")
        operation = str('Addition')
        self.arithmetic_operation = operation
    
    # registers subtraction unto variable operation
    def intro_sub(self):
        print("\nYou chose subtraction")
        operation = str('Subtraction')
        self.arithmetic_operation = operation

    # registers multiplication unto variable operation
    def intro_mul(self):
        print("\nYou chose multiplication")
        operation = str('Multiplication')
        self.arithmetic_operation = operation

    # registers division unto variable operation
    def intro_div(self):
        print("\nYou chose division")
        operation = str('Division')
        self.arithmetic_operation = operation 
        
    # registers exponentiation unto variable operation
    def intro_exp(self):
        print("\nYou chose exponentiation")
        operation = str('Exponentiation')
        self.arithmetic_operation = operation

    # registers square root unto variable operation
    def intro_sqrt(self):
        print("\nYou chose square root")
        operation = str('Square Root')
        self.arithmetic_operation = operation

    # registers cube root unto variable operation
    def intro_cbrt(self):
        print("\nYou chose cube root")
        operation = str('Cube Root')
        self.arithmetic_operation = operation 

    # method to print results in an animated way
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