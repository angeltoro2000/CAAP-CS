# imports multiple clases from the python library and some of our
# own modules.

from sys import exit
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine

# global variables to keep track of score, player, and leaderboard

moves = 0
name = ""
leaderboard = Leaderboard()


# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard

def game_over(won):
    global name
    global moves
    score = Score(name, moves)

    if (won):
        leaderboard.update(score)
        print("\nYou won")
        leaderboard.print_board()

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.

def play_game():
    while True:
        global name
        global moves
        print ("Welcome to my How to survive college game! To quit enter :q at any time. You will have three lives. Good luck!")
        name = input("\nLet's play. Enter your name. > ")
        if (name == ':q'):
            exit(1)
        dificulty_level=""
        while True:
            dificulty_level=str(input("Which dificulty do you want: Easy, Medium or hard?"))
            if dificulty_level=="easy" or dificulty_level=="medium" or dificulty_level=="hard":
                break
            else:
                print("Not one of the levels")
        a_map = Map('oweek-scene')
        a_game = Engine(a_map, dificulty_level)
        moves = a_game.play()
        game_over(a_game.won())


play_game()

def test_game():
    test_playgame=game_over()
    test_playgame2=play_game()
test_game()