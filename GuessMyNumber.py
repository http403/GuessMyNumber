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
        print(f"Guess a number between {lower_bound} and {upper_bound}")
        print()

        target: int = random.randint(lower_bound, upper_bound)
        attempt: int = 1
        while True:
            guess: int = prompt(f"#{attempt} Try")
            if guess < target:
                print("Too low, try again!")
                attempt += 1
            elif guess > target:
                print("Too high, try again!")
                attempt += 1
            elif guess == target:
                print(f"Congratulation! You got my number in {attempt} {'try' if attempt == 1 else 'tries'}.")
                break
        again = prompt('Play again', 'str')
        if again.lower() in ['n', 'no']:
            break

    print("Thanks for playing. Goodbye.")
    pass


if __name__ == '__main__':
    main()
