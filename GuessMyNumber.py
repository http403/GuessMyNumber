import random
from typing import Union


# An improved prompting with fixed style and error handling
def prompt(p, data_type='int') -> Union[str,int]:
    prompted: str = input(f"{p}> ")
    if data_type == 'int':
        while True:
            try:
                return int(prompted)
            except (EOFError, ValueError):
                print("That's not something you suppose to type in!")
    else:
        return prompted


class Game:
    def __init__(self):
        self._target: int = 0

        self._lower_bound: int = 1
        self._upper_bound: int = 10
        self._greet_string: str = 'Welcome to the Guess My Number'
        self._quit_string: str = 'Thanks for playing this game!'

    @property
    def greetings(self) -> str:
        return self._greet_string

    def start_game(self) -> None:
        print(self.greetings)

        while True:
            print(f"Guess a number between {self._lower_bound} and {self._upper_bound}")
            print()

            self._target = random.randint(self._lower_bound, self._upper_bound)
            attempt: int = 1
            while True:
                n: int = prompt(f"#{attempt} Try")
                if n < self._target:
                    print("Too low, try again!")
                    attempt += 1
                elif n > self._target:
                    print("Too high, try again!")
                    attempt += 1
                elif n == self._target:
                    print(f"Congratulation! You got my number in {attempt} {'try' if attempt == 1 else 'tries'}.")
                    break
            again = prompt('Play again', 'str')
            if again.lower() in ['.', 'n', 'no']:
                break


if __name__ == '__main__':
    game = Game()
    game.start_game()
