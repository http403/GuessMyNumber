import random
from typing import Union

lower_bound = 1
upper_bound = 10


# An improved prompting with fixed style and error handling
def prompt(p, data_type = 'int') -> Union[str,int]:
    prompted: str = input(f"{p}> ")
    if data_type == 'int':
        while True:
            try:
                return int(prompted)
            except (EOFError, ValueError):
                print("That's not something you suppose to type in!")
    else:
        return prompted


# The main logic
def main():
    print("Welcome to the Guess My Number!")

    while True:
        target: int = random.randint(lower_bound, upper_bound)
        while True:
            guess: int = prompt(f"Guess a number between {lower_bound} and {upper_bound}")
            if guess < target:
                print("Too low, try again!")
            elif guess > target:
                print("Too high, try again!")
            elif guess == target:
                print("Congratulation! You got my number.")
                break
        again = prompt('Play again', 'str')
        if again.lower() in ['n', 'no']:
            break

    print("Thanks for playing. Goodbye.")
    pass


if __name__ == '__main__':
    main()
