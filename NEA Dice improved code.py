from operator import itemgetter
from random import randint
from time import sleep

# Used as a separator for each round, purely to be aesthetically pleasing
SEP = '------------------------------------------'

CREDENTIALS = {
        'user': '2369',
        'admin': '1642',
}


def get_logged_on_player(credentials, exclude_players=set()):
    """Ask a user for their name and their PIN and return the username
    if successfully authenticated.

    This function checks the :credentials: dictionary for valid usernames
    and ask the players to authenticate using their PIN. Keep asking until
    a valid username and the corresponding PIN are entered by a player.

    If a provided username is found in :exclude_players:, this function
    forbids them for logging again.
    """

    player_id = f"Player {len(exclude_players) + 1}:"
    while True:
        username = input(f"{player_id} Please enter a valid username: ").lower()
        if username in exclude_players:
            print('Someone is already logged in by that username!')
            continue
        if username not in credentials:
            print('A user by that username was not found!')
            continue
        pin = credentials[username]
        pin = input(f"{player_id} Please enter the PIN for {username.capitalize()}: ")
        if pin == credentials[username]:
            print("Welcome ", username.capitalize(), "! You're now logged in.", sep='')
            return username
        print("Invalid PIN! Please try again")


def roll(tie_breaker: bool=False):
    """Roll a dice and perform the required actions

    Rules define the following actions:
     - add the first two dice to get the initial amount of points
     - first two dice add up to an even number => +10 points
     - first two dice add up to an odd number => -5 points
     - first two dice are equal => add the value of the third die to the points

    If the tie_breaker mode is requested, only return the value of a single die.
    """

    if tie_breaker:
        return randint(1, 6)

    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    roll3 = randint(1, 6)

    score = roll1 + roll2
    score += 10 if score % 2 == 0 else -5
    if roll1 == roll2:
        score += roll3

    return max(score, 0)


def display_score(username: str, points: int):
    """Pretty prints how much point a user gained in a round"""

    if points > 0:
        print(username, 'has gained', points, 'points')
    else:
        print(username, 'did not gain any additional points')


def play_a_round(players, round_number=None):
    """Simulate a round of the dice roll game

    Display the scores along the way and a summary of the
    scores so far at the end of the round.

    If no :round_number: is provided, simulate a tie-breaking round
    """

    input(f"Press Enter to proceed to round {round_number or 'tie-breaking'}")
    print("Rolling Die...")
    sleep(0.5)  # Cosmetic pause, add dramatic effect
    print(f"{SEP}\nRound No: {round_number or 'tie-breaking'}")

    for player in players:
        score = roll(bool(round_number))
        display_score(player, score)
        players[player] += score

    # Roll our own `max` implementation to search for draws
    # Use the loop to display scores as well
    print(SEP)
    best_score = 0
    best_player = None
    for player, score in players.items():
        print(player, "'s Score: ", score, sep='')
        if score > best_score:
            best_score = score
            best_player = player
        elif score == best_score:
            best_player = None

    print(f"    ||    Currently Winning Player: {best_player or 'DRAW'} (score {best_score})\n{SEP}")
    return best_player


def play(player_count=2, rounds=5):
    """Run several rounds of the dice roll game and return the overall winner"""

    print("Welcome!\nYou need to be logged in to access this game.")
    players = {}
    while len(players) < player_count:
        player = get_logged_on_player(CREDENTIALS, players)
        players[player] = 0

    for r in range(rounds):
        winner = play_a_round(players, r + 1)

    while winner is None:
        print("It seems to be a draw; tie breaker mode will now be activated.")
        print("This means that each user will now only have 1 roll each and any odd/even bonuses will not be applied henceforth.")
        winner = play_a_round(players)

    score = players[winner]
    print("🎉 WE HAVE A WINNER! 🎉")
    print(f"{SEP}\n\n{winner.capitalize()} has won the game with their score of {score}!\n")

    return winner, score


def save_winner(winner, score, filename='winners.txt'):
    """Add a new entry to the provided file with a new winner

    Added entry is a single line of the form
    PlayerName:PlayerScore
    """

    with open(filename, 'a') as f:
        print(winner, score, sep=':', file=f)


def leaderboard(filename='winners.txt', limit=5):
    """Read from the provided file and prints the best :limit: players

    INTENDED LINE FORMAT FOR EXTERNAL FILE:
    PlayerName:PlayerScore

    If the external file is manually edited to a format different to
    this, it will result in the production of error(s).
    """

    scores = []
    with open(filename) as f:
        for line in f:
            name, score = line.rsplit(':', 1)
            scores.append([name, int(score)])

    leaderboard = sorted(scores, key=itemgetter(1), reverse=True)[:limit]
    print("Top", limit, "scores (loaded from", filename, "):")

    for i, (name, score) in enumerate(leaderboard, start=1):
        print(i, ". ", name.capitalize(), " (", score, " points)", sep='')

    # Add missing entries to always have a display of :limit: items
    for i in range(len(leaderboard), limit):
        print(i + 1, ". -- No Data Found --", sep='')


if __name__ == '__main__':
    winner, score = play()
    save_winner(winner, score)
    leaderboard()
