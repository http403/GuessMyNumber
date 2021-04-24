import random

lower_bound = 1
upper_bound = 10


# An improved prompting with fixed style and error handling
def prompt(p) -> int:
    while True:
        try:
            return int(input(f"{p}> "))
        except (EOFError, ValueError):
            print("That's not something you suppose to type in!")


# The main logic
def main():
    # print("Welcome to the Guess My Number!")
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
    print("Thanks for playing. Goodbye.")
    pass


if __name__ == '__main__':
    main()
