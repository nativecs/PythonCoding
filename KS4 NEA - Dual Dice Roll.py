from random import randint  # import the randint function from the random package; can be accessed via randint()
from typing import List  # support for type annotations (prevents  my linter from throwing errors)
from time import sleep  # import sleep from the time module
from operator import \
    itemgetter as ItemGetter  # Import the itemgetter module; this makes it easier to manipulate 2 dimensional lists. represents a callable object that fetches the given item(s) from its operand.

usernames = ['user', 'admin']  # list of valid usernames;
pins = ['2369', '1642']  # list of valid PINS (PIN for usernames[0] is pins[0]);
active_players = []  # List of active players, prevents a user from logging in twice under the same username
rounds = 0  # int | Number of rounds that have passed, used to ensure only 5 rounds have gone before a winner is determined
# Initiate score trackers for both players.
player1_score = 0
player2_score = 0
carry_on = True  # Whether or not rounds should be ran
# Initiate tracker for the winner's name and score
winning_player = None
winning_score = None
tie_breaker = False  # Whether tie breaker (tie_breaker) mode is enabled
sep = '------------------------------------------'  # used as a separator for each round, purely to be aesthetically pleasing


class InputMessages:
    username: str = f"Player $playernum: please enter a valid username: "
    pin: str = f"Player $playernum: please enter the PIN for $player: "
    welcome: str = f"\nWelcome $player, you've successfully logged in!"


print("Welcome!\nYou need to be logged in to access this game.")
while len(active_players) < 2:  # while the number of usernames in the active_players list is less than 2:
    # input and validate username:
    _id = f"(Player {len(active_players) + 1}): "
    username = str(input(f"{_id}Please enter a valid username: ")).lower()
    while username in active_players:  # if the username is in the active_users list, completely prevent the user from logging in as that user by creating a loop that can only be broken if the user enters a username that is not in this list;
        print(f'Someone is already logged in by that username!')
        username = str(input(
            f"{_id}Please enter a valid username: ")).lower()  # re-assign the new inputted value to the username var, allowing the loop to break if the user has entered a valid username (that is not already taken;
    while not username in usernames:  # If a username is not in the usernames list, create a loop which will ask the user to re-input a valid username

        print(f'A user by that username was not found!')
        username = str(input(
            f"{_id}Please enter a valid username: ")).lower()  # re-assign to the new inputted value to "username", allowing the loop to break if the user has entered a username that is not in the active_players list.
    username_index = usernames.index(
        username)  # Find the "username" that the user has enterd's position in the pins list. This will allow me to check if the pin provided is the CORRECT pin for the user identified;
    # check pin (relative to the username inputted above)
    pin = str(input(
        f"{_id}Please enter the PIN for {username.capitalize()}: "))  # prompt user to input their "pin" (Type: str)
    while not pins[
                  username_index] == pin:  # If the pin for the identified user is incorrect, instantiate a loop asking user to input the correct PIN
        print(f"Invalid PIN! Please try again")
        pin = str(input(
            f"{_id}Please enter the PIN for {username.capitalize()}: "))  # re-assign the new inputted value so the loop takes the new value into account
    print(f"{_id}Welcome {username.capitalize()}! You're now logged in.")
    active_players.append(username)  # Add the username to the end of the active_users list

player1 = active_players[
    0].capitalize()  # Assigns the active_players[0] username to the player1 variable, purely for convenience
player2 = active_players[
    1].capitalize()  # Assigns the active_players[1] username to the player2 variable, purely for convenience

'''
This function will roll a dice and perform the required actions upon the returned value (if even, +10, if odd, -5 etc)
param {bool} Tie_breaker: Whether or not tie breaker mode is active
'''


def roll(Tie_breaker: bool = False):
    if Tie_breaker == True:  # If the Tie_breaker boolean param is True, only return 1 random int between 1 and 6 (tie breaker mode rules)
        return randint(1, 6)
    score = 0  # The final number of points that the <user> has scored.
    # Generate a random number between 1 and 6
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    roll3 = randint(1, 6)
    score = roll1 + roll2  # Add together all of the rolls and store them under one variable, making it easier to manipulate;
    if score % 2 == 0:  # Check if the score is an even number; % just divides the number and returns the remainder of the division;
        # Even number, +10 to the user's score.
        score += 10
    else:
        score -= 5  # User rolled an odd number; -5 from their score
    if score < 0:  # Checks if the int score is less than 0; if it is, set it to 0
        score = 0
    if roll1 == roll2:  # If roll1 equates to roll2, then add the value of roll3 to the final, total score
        score += roll3
    return score


'''
The following function will return either None, 1 or 2 depending on who out of the 2 players now has the highest score
param: {int} score1 --> Player 1's Score to take into account; 
param: {int} score2 --> Player 2's Score to take into account 
returns: 
    --> 1 IF score1 > score2
    --> 2 IF score2 > scrore1
    --> None IF score1 == score2
'''


def identify_winner(score1: int, score2: int):
    if score1 == score2:  # If score 1 is equal to score2, it is a draw:
        return None
    # elif acts as a shorthand for else if
    elif score1 > score2:  # Player 1 has a higher score than player 2; return 1.
        return 1
    else:  # Player 2's score is greater than player 1's score; return 2.
        return 2


while rounds < 5 or tie_breaker == True and (
        carry_on == True):  # Instantiate a loop: this will continue if the number of rounds (rounds) is less than 5 **OR** if tie breaker (tie_breaker) is set as True **AND** if carry on is as True. Since this part is in parenthesis, this will be checked first
    rounds += 1  # Increment number of rounds
    input(f"Press Enter to proceed to round {rounds} ")
    print("Rolling Die...")
    sleep(0.5)  # wait for 1/2 seconds [just to add effect];
    print(sep)
    print(f"Round No: {rounds}")
    if tie_breaker != True:  # make sure that 2 dice are only rolled if tie breaker mode is not active.
        # Roll die and perform actions based on the number
        player1_scored = roll()
        player2_scored = roll()
        # Add the amount of points scored to the player who scored them
        player1_score += player1_scored
        player2_score += player2_scored
    else:  # If the above condition if False, then we know that tie breaker mode is active.
        # Call the roll function with the tie_breaker param as True
        player1_scored = roll(True)
        player2_scored = roll(True)
        player1_score += player1_scored
        player2_scored += player2_scored
    new_winner = identify_winner(player1_score,
                                 player2_score)  # Utilise the identify_winner() function and determine a winner by the result of this function;

    if new_winner == None:  # If None is returned, THEN there is a DRAW;
        winning_player = 'DRAW'  # set the winning_player to draw; this will be displayed below;
        winning_score = player1_score
    elif new_winner == 1:
        winning_player = player1  # set the winning player as player1
        winning_score = player1_score
    else:
        winning_player = player2  # set the winning player as player2
        winning_score = player2_score

    #     Utilise the "ternary" (compressded if statements) operator to reduce the hassle of a huge if-elseif-else block.
    player1_display_gained_points = "did not gain any additional points" if player1_scored == 0 else f"has gained {player1_scored} points"
    player2_display_gained_points = "did not gain any additional points" if player2_scored == 0 else f"has gained {player2_scored} points"
    print(f"{player1} {player1_display_gained_points}")
    print(f"{player2} {player2_display_gained_points}")
    print(sep)
    print(f'''
{player1}'s Score: {player1_score}
{player2}'s Score: {player2_score}
    ||    Currently Winning Player: {winning_player} (score {winning_score})
{sep}
    ''')

    if rounds >= 5:  # IF the number of rounds incurred (rounds) is greater than or equal to 5, attempt to determine a winner or start tie breaker;
        if new_winner != None:  # Only attempt to determine a winner if new_winner != None, ensuring that it is NOT a draw
            print("🎉 WE HAVE A WINNER! 🎉")
            print(sep)
            print(f'''
{winning_player} has won the game with their score of {winning_score}!
            ''')
            # Prevent further rounds from being ran =>
            carry_on = False
        else:
            # Enable tie breaker mode
            print("It seems to be a draw; tie breaker mode will now be activated.")
            print(
                "This means that each user will now only have 1 roll each and any odd/even bonuses will not be applied henceforth.")
            if tie_breaker != True:
                tie_breaker = True

'''
INTENDED FORMAT FOR EXTERNAL FILE:
PlayerName:PlayerScore
where PlayerName represents a player's name 
where PlayerScore represents a player's score
    - If the external file is manually edited to a format different to this, it will result in the production of error(s) 
'''
to_w = f"{winning_player}:{winning_score}"  # What to write to the external file

# Use python with open() to open the file, as target followed by a block of code.
# This reduces how cluttery the code is and makes it easier to manage resources, such as file streams as utilised below:
# List of all winners, read from ext file and the winner of this game

winners = []  # this will be the new content of the external file
# This code will prevent the write file to completely wipe it each time; it will create some sort of persistence in regards to data in that file.
with open('./winners.txt', 'r') as f:
    for line in f.readlines():
        # for each line in the file:
        # add the line into the winners list, ensuring \n (newline character) is removed
        winners.append(line.replace('\n', ''))
    winners.append(to_w)  # add the winner of this game
    f.close()  # close file

with open('./winners.txt', 'w') as f:
    f.write('\n'.join(winners))  # write to the file;
    f.close()  # Close the file after it has been written to.

data = []  # This will be the final, formatted, ready-to-sort list

for w in winners:  # for every value in the winner_cache list:
    data.append(
        [str(w.split(':')[0]), int(w.split(':')[1])])  # create a new 2d list with the name and the score of the player
# Now we sort the data based on the int score
# Utilise python slice notation on the returned list -->
sorted_data = sorted(data, key=ItemGetter(1), reverse=True)[:5];

# map through the list, converting the end result to a list.
msg = list(map(lambda arg: f"{arg[0].capitalize()} ({arg[1]} points)", sorted_data))

print(f"Top 5 scores:\n(loaded from ./winners.txt)")
printed = 0  # Amount of printed scores

# Loop through the printing of each player name and score
for x in range(0, len(sorted_data)):
    printed += 1
    print(str(x + 1) + '.', msg[x])  # --> 1. Userz (10 points)
    #     2. Admin (5 points)
    #   ...

# Print that not data is found if no data is found - simply reduces confusion for the End User
while printed < 5:  # count controlled loop; only run while printed less than (<) 5
    printed += 1
    print(f'{printed}. -- No Data Found --')