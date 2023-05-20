# UI class
# creates class
class UI:
    def __init__(self, operation) -> None:
        print("Welcome to the Calculator!")
        self.operation = operation

    def start():
        print("Welcome to the Calculator!")

    def intro_add(self):
        print("\nYou chose addition")
        self.operation = 'Addition'

    def intro_sub(self):
        print("\nYou chose subtraction")
        self.operation = 'Subtraction'

    def intro_mul(self):
        print("\nYou chose multiplication")
        self.operation = 'Multiplication'

    def intro_div(self,):
        print("\nYou chose division")
        self.operation = 'Division'

    def animated(self):
        print('\nOperation')
        time.sleep(1)
        print(f': {self.operation}')
        time.sleep(1.5)
        print(f"Numbers to be computed")
        time.sleep(1)
        print(f': {firstN, secondN}')
        animation = '...'
        for i in range(len(animation)):
            print(animation[i], end='', flush=True)
            time.sleep(1.5)
        # Print the Result
        print(f"\n\nHere is your result\n:{result}")
