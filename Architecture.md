# Architecture

## Player perspective

The player should be greeted. Then if first time start up, game will ask them for a game tag then main menu. Otherwise,
stright hop to the main menu. From there, 4 options available Solo, Multiplayer, Settings, and Exit Solo is the game mode
play against computer AI, where online is against other actuall player. Settings is used to tweak the local computer AI
parameters.

## Solo

After the player selected solo play mode, he will be instantly greeted by the computer AI with current settings
displayed. Then the game will proceed like typical Guess the Number. The player can keep trying until he got the right
answer or tries ran out. After that, results will be displayed and ask if he wants to try again. If he chooses to try
again, display will switch back to the AI greeting screen and the game starts again. Otherwise, back to the main menu.

### Multiplayer

The player will have 3 options here: Play, Host, and Back. Play mode is for connecting to other player (host) and
challenge them where Host mode is the player become a host of the game and able to accept (or reject) challenges.

#### Play mode

It's largely the same flow in solo. Only 2 exceptions exists. First, the player (challenger) need to type in the IP
address of the host. Second, if the challenger wants to retry, host must accept the challenge again in order to proceed.

#### Host mode

The player now become the host. If the selection of Host, the player will have the option to set up custom rules for
Multiplayer mode. Solo setting will be used if that is the first time for the program be host, then the new settings will be saved separately for
the future. After setting up the rules, network information required to connect to the host will be displayed (and such
data should be passed to player who's willing to join). Then the game will automatically listen for incoming connection
for challenge. Host have the option of quiting while waiting for challenger. When challenger comes in, host will have
the options to reject the challenge. If accepted, host is being prompted to enter a number as the target. Then there
will be nothing left for the host to do. The game will automatically handle the rest, until the next challenger shows
up. (TODO: Give more work to the host).

### Settings

Setting page is the place where the player can change their game tag and the local AI behaviour like the lower and upper
bound of guessable range, and tries limited mode.

## Code Structure

The game consist of one entrypoint `main()` and two main class: Challenger and Host. Then two classes: RealHost and
AIHost, will be created with Host class inheritance.

### `main()`

This is the program entrypoint where it will decide what classes need to be initialized. And responsible for the initial
greeting, and ultimate error handling.

### Challenger Class

This class contains all required interaction for to the player such as inputting the guessed number, network connection,
and any message feedback.

### Host Class

This class is an abstract class that define the needed methods for RealHost and AIHost. It contains the networking, and
verification code.

#### RealHost

This is the class intended to be used by real human host, and included with prompts for entering information, and verification.

### AIHost

This is the class that deal with local play. It should only be used if player select solo game mode. It contains the
random number selector, and verification