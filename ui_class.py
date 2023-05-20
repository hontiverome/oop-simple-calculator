# UI class
# creates class
class UI:
    def start():
        print("Welcome to the Calculator!")

    def intro_add():
        print("\nYou chose addition")
        operation = str('Addition')

    def intro_sub():
        print("\nYou chose subtraction")
        operation = str('Subtraction')

    def intro_mul():
        print("\nYou chose multiplication")
        operation = str('Multiplication')

    def intro_div():
        print("\nYou chose division")
        operation = str('Division')

    def animated():
        print('\nOperation')
        time.sleep(1)
        print(f': {operation}')
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
