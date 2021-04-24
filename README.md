# Guess My Number

## tl;dr: an overcomplicated version of the typical Guess the Number game.

This is not my first attempt in code this game, but my first attempt to add networking functionality to it. For me, it is
like a practice.

## TODO
Just a list keeping me in track.

### Essential
Things that must be done.

- [x] Basic Game
  - [x] Guess number between 1 to 10
  - [x] Matching with loops
  
### Expansion
Things instructor suggested, or I want to add in the future.

- [ ] Instructor suggested
  - [x] Allow the user to change the range of numbers to choose from (such as 1-100 or 1-1000)
  - [ ] Keep track of the number of attempts needed
  - [ ] Add a "Play again?" option at the end
  - [ ] Add a leader board that tracks successes
    - [ ] Track player with not only succession (under default unlimited guess mode, every player will succeed)
      - [ ] Track player in numbers of tries
  - [ ] Create multiple levels with increasing difficulty at each level
- [ ] Networking
  - [ ] Local P2P
  - [ ] Multiplayer
    - [ ] Host multiple games by one player
    - [ ] Random number suggestion for aiding host
  - [ ] Locked Games
  - [ ] Encrypted Sessions
  - [ ] Over the Internet
  - [ ] Matching Server
  - [ ] Chat system
- [ ] Improved Hinting
  - [ ] Adjective (litte/much/too/etc.)
  - [ ] Vague description word (e.g.: third number is curly with no openings)
    - [ ] Manual Hint Input per Round
    - [ ] Auto select pre-written hints
  - [ ] Limited Hint
  - [ ] Manual Hint Input per Game
- [ ] Points/Score System
  - [ ] Pair with Matching Server to create global leader board