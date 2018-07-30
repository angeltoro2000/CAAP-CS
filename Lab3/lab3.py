# Angel Toro
# LAB3

from random import randint

# ladder=up
# chute=down

# creates given dimensions for the matrix
# function that plays a game
# one in which it takes in dice roll from user and one that plays itself
# after all that, code one that says moves


# global variable of chutes and ladders
# remember to let your function know you're using this variable with 'global'
chutes_ladders = {4: 7,
				  8: 15,
				  12: 2,
				  14: 6}


# Rolls a die of six sides and returns the result
def roll_die():
	die= (randint(1, 6))
	return die


# makes a game (just a list) of the given dimensions
def makeGame(w, l):

	game_list = []
	for i in range((w * l)):
		game_list.append(i + 1)
	return game_list





# checks if given square is a chutes or ladders
def is_chutes_ladders(d):
	global chutes_ladders
	for i in chutes_ladders:
		if i==d:
			return True
		return False
# function to make and play a game

def play_game(gamemode, w,l):
	print("Let's play chutes and latters")
	gamemode=input("What game mode do you want to play? player or computer: ")

	if gamemode=="player":

		w=int(input("Enter a width: "))
		l=int(input("Enter a length: "))
		makeGame(w,l)
		players=int(input("How many players?"))
		state=[]
		for i in range(players):
			players_name=input("What is player %s's name"%(i+1))
			state.append({"Player":players_name, "Place":1, "Moves":0})
		print(state)
		gameover=False
		while gameover==False:
			for playing in range(players):
				print("It is Player",playing+1,"'s turn")
				roll=input("press any key to roll")
				die=roll_die()
				print("you rolled a", die,".")
				state[playing]["Place"]+=die
				state[playing]["Moves"]+=1
				print("You are now in",state[playing]["Place"],".")
				if state[playing]["Place"] in chutes_ladders:
					state[playing]["Place"]=chutes_ladders[state[playing]["Place"]]
				if state[playing]["Place"]>(w*l):
					gameover==True
					state[playing]["Place"]==w*l
					print("PLayer "+str(playing+1)+": You won!")
					gameover=True

					break
	else:
		makeGame(w,l)
		position=1
		moves=0
		while position<(w*l):
			position+=roll_die()
			moves+=1
			if position in chutes_ladders:
				position=chutes_ladders[position]
			if position >= (w*l):
				print(moves, "Moves")
				break



	#

	#for loop and let input how many players you will need to store the value for
	#state=0
	#when state increase, then you move through the index of the array
	#unless a chute or latter, then it index move to the value of the dictionary
	#
	#when the index of the array is bigger than 36 the person has won.

# Runs the game as a simulation and keeps track of the number of moves it takes to win and returns average

def simulate_game():
	#it prints the amount of moves it took the first person to do.
	#after several runs, it allows you to see the average
	#formula
	w=int(input("Enter a width: "))
	l=int(input("Enter a length: "))
	times=int(input("How many times do you plan on running the game?"))
	sums=[]
	for i in range(times):
		sums.append(play_game(2,l,w))
		return sums
	print("The average number of moves the simulation found were",sum(sums)/len(sums),"moves.")

simulate_game()