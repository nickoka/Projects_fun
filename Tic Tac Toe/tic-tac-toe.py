"""
Unbeatable Tic-Tac-Toe:
This game will involve the user to play first with any game piece
the user wants to play with. The user will play against an AI that
is unbeatable. The worst case scenario for the AI is a tie. The user
will not be able to win. (Assuming the program works as described).

If the user does win, there is an error in the program and will hopefully
be fully fixed as time goes on.

Below is a how the gameboard will be displayed:

 0 | 1 | 2
 ---------
 3 | 4 | 5
 ---------
 6 | 7 | 8

Author:
Nick Oka
nickoka1250@gmail.com

Created in Spring 2019

Credits:

Resource used for tic-tac-toe strategy:
https://www.instructables.com/id/Winning-tic-tac-toe-strategies/

Usage: 

python3 tic-tac-toe.py

"""

import random

# keep track of the current game board
board_spots = [0, 1, 2, 3, 4, 5, 6, 7, 8]
corners = [0, 2, 6, 8]
sides = [1, 3, 5, 7]

def playGame():

	print("\nWelcome to the Unbeatable Tic-Tac-Toe Game!")

	print("X's or O's? Or any other character. ")

	player_item = input()

	opp_item = "X"

	if (player_item == opp_item):
		opp_item = "O"

	print("Try to win!\n")
	print("Here's the board: (Choose your spot with the corresponding spot number)\n")
	printBoard()

	played_spots = [] # track the moves made by the player

	player_played_spots = []

	ai_spots = []

	curr_game = [
		["zero", "three", "six"],
		["one", "four", "seven"],
		["two", "five", "eight"],
		["zero", "one", "two"],
		["three", "four","five"],
		["six", "seven", "eight"],
		["zero", "four", "eight"],
		["two", "four", "six"]]

	curr_game_opp = [
		["zero", "three", "six"],
		["one", "four", "seven"],
		["two", "five", "eight"],
		["zero", "one", "two"],
		["three", "four","five"],
		["six", "seven", "eight"],
		["zero", "four", "eight"],
		["two", "four", "six"]]

	numMove = 0

	while True:

		while True:

			move = int(input("Player, enter a spot to play (0-8): "))
			if move in corners:
				corners.remove(move)
			elif move in sides:
				sides.remove(move)
			if move not in played_spots:
				played_spots.append(move)
				player_played_spots.append(move)
				curr_game = playPiece(curr_game, player_item, move)
				print()
				printBoard()
				break
			else:
				print("\nSpot already played. Try again.")

		if ifWin(curr_game):
			print("You win!\n")
			break

		if len(played_spots) == 9:
			print("It's a tie!")
			break

		while True:

			move = aiMove(player_item, opp_item, played_spots, player_played_spots, 
					curr_game_opp, curr_game, numMove)
			if move == None:
				break
			elif move in corners:
				corners.remove(move)
			elif move in sides:
				sides.remove(move)
			if move not in played_spots:
				played_spots.append(move)
				curr_game_opp = playPiece(curr_game_opp, opp_item, move)
				print("The opponent has played in spot {}".format(move))
				print()
				printBoard()
				break
			else:
				print("\nSpot already played. Try again.")
		numMove += 1

		if len(played_spots) == 9 or move == None:
			print("It's a tie!")
			break

		if ifWin(curr_game_opp):
			print("The opponent wins!\n")
			break

	return

# print the current gameboard
def printBoard():
	print("{} | {} | {}".format(board_spots[0], board_spots[1], board_spots[2]))
	print("---------")
	print("{} | {} | {}".format(board_spots[3], board_spots[4], board_spots[5]))
	print("---------")
	print("{} | {} | {}\n".format(board_spots[6], board_spots[7], board_spots[8]))

# given the move, play the move on the gameboard
def playPiece(curr_game, player, move):

	outer_count = 0
	for outer in curr_game:
		inner_count = 0
		for inner in outer:
			if inner == "zero" and move == 0:
				curr_game[outer_count][inner_count] = 0
				board_spots[move] = player
			elif inner == "one" and move == 1:
				board_spots[move] = player
				curr_game[outer_count][inner_count] = 1
			elif inner == "two" and move == 2:
				board_spots[move] = player
				curr_game[outer_count][inner_count] = 2
			elif inner == "three" and move == 3:
				board_spots[move] = player
				curr_game[outer_count][inner_count] = 3
			elif inner == "four" and move == 4:
				board_spots[move] = player
				curr_game[outer_count][inner_count] = 4
			elif inner == "five" and move == 5:
				board_spots[move] = player
				curr_game[outer_count][inner_count] = 5
			elif inner == "six" and move == 6:
				board_spots[move] = player
				curr_game[outer_count][inner_count] = 6
			elif inner == "seven" and move == 7:
				board_spots[move] = player
				curr_game[outer_count][inner_count] = 7
			elif inner == "eight" and move == 8:
				board_spots[move] = player
				curr_game[outer_count][inner_count] = 8
			inner_count += 1
		outer_count += 1

	return curr_game

# ai chooses the best next move to play against the user
def aiMove(player_item, opp_item, played_spots, player_played_spots, 
	curr_game_opp, curr_game, numMove):
	
	if (numMove == 0):
		if (4 not in played_spots):
			return 4
		else:
			if corners != []:
				return random.choice(corners)

	else:

		# check if the ai has a chance to win
		for x in curr_game_opp:
			counter = 0
			if (type(x[0]) is int and type(x[1]) is int and type(x[2]) is str):
				move = convert(x[2])
				if move not in played_spots:
					return move
			elif (type(x[0]) is int and type(x[2]) is int and type(x[1]) is str):
				move = convert(x[1])
				if move not in played_spots:
					return move
			elif (type(x[2]) is int and type(x[1]) is int and type(x[0]) is str):
				move = convert(x[0])
				if move not in played_spots:
					return move

		# check if the player has a chance to win - block if does
		for x in curr_game:
			if (type(x[0]) is int and type(x[1]) is int and type(x[2]) is str):
				move = convert(x[2])
				if move not in played_spots:
					return move
			elif (type(x[0]) is int and type(x[2]) is int and type(x[1]) is str):
				move = convert(x[1])
				if move not in played_spots:
					return move
			elif (type(x[2]) is int and type(x[1]) is int and type(x[0]) is str):
				move = convert(x[0])
				if move not in played_spots:
					return move

	# second move for the ai when the player is in the center spot
	if (numMove == 1 and 4 in player_played_spots):
		if corners != []:
			return random.choice(corners)

	# ai goes for the corners over the sides
	else:
		if sides != []:
			if corners != []:
				return random.choice(corners)
		else:
			if sides == []:
				if corners != []:
					return random.choice(corners)
			else:
				return random.choice(sides)
	return

# helper to convert the number in text form to the number
def convert(text):

	if (text == "zero"):
		return 0
	elif (text == "one"):
		return 1
	elif (text == "two"):
		return 2
	elif (text == "three"):
		return 3
	elif (text == "four"):
		return 4
	elif (text == "five"):
		return 5
	elif (text == "six"):
		return 6
	elif (text == "seven"):
		return 7
	elif (text == "eight"):
		return 8

# check if the player/opponent has won the game
def ifWin(curr_game):

	winning_combos = [
		[0, 3, 6],
		[1, 4, 7],
		[2, 5, 8],
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8],
		[0, 4, 8],
		[2, 4, 6]]

	for combo in curr_game:
		if combo in winning_combos:
			return True

	return False

def main():

	playGame()

main()
