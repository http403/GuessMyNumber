import random
from typing import Union


# An improved prompting with fixed style and error handling
def prompt(p, data_type='int') -> Union[str, int]:
    while True:
        prompted: str = input(f"{p}> ")
        if data_type == 'int':
            try:
                return int(prompted)
            except (EOFError, ValueError):
                print("That's not something you suppose to type in!")
        else:
            return prompted


class Game:
    def __init__(self):
        self._target: int = 0
        self._attempt: int = 1

        self._lower_bound: int = 1
        self._upper_bound: int = 10
        self._greet_string: str = 'Welcome to the Guess My Number'
        self._quit_string: str = 'Thanks for playing this game!'

        self.roll_target()

    @property
    def attempt(self) -> int:
        return self._attempt

    @property
    def greet_string(self) -> str:
        return self._greet_string

    @property
    def quit_string(self) -> str:
        return self._quit_string

    @property
    def lower_bound(self) -> int:
        return self._lower_bound

    @property
    def upper_bound(self) -> int:
        return self._upper_bound

    def again(self) -> None:
        self.roll_target()
        self._attempt_reset()

    def roll_target(self) -> None:
        self._target = self._roll()

    def guess(self, n) -> int:
        if n < self._target:
            self._attempt += 1
            return -1
        if n > self._target:
            self._attempt += 1
            return 1
        if n == self._target:
            return 0

    def _roll(self) -> int:
        return random.randint(self._lower_bound, self._upper_bound)

    def _attempt_reset(self) -> None:
        self._attempt = 1


if __name__ == '__main__':
    # Display and user interactions happens here
    game = Game()

    print(game.greet_string)
    while True:
        print(f"Guess a number between {game.lower_bound} and {game.upper_bound}")
        print()

        while True:
            attempt: int = game.attempt
            guess: int = prompt(f"#{attempt} Try")
            result = game.guess(guess)
            if result < 0:
                print("Too low, try again!")
            if result > 0:
                print("Too high, try again!")
            if result == 0:
                print(f"Congratulation! You got my number in {attempt} {'try' if attempt == 1 else 'tries'}.")
                break
        again: str = prompt("Play again? (./n/no to stop)", 'str')
        if again.lower() in ['.', 'n', 'no']:
            break
        else: game.again()

    print(game.quit_string)