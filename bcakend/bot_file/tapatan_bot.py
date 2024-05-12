# Tapatan Bot By Tugas Artificial Intelligence IT 2024 Week 6

import random

patt = 0
oatt = 0

# player piece && opponent piece
player_p, opponent_p = "O", "X"

## MINIMAX ALGORITHM
 
def find_move(board, piece_row, piece_col) :
	all_move = []

	if(piece_row >= 0 and piece_col >= 0) :
		# check move to left
		if(piece_col - 1 >= 0) :
			if(board[piece_row][piece_col - 1] == "_") :
				all_move.append(-1)
		
		# check move to up
		if(piece_row - 1 >= 0) :
			if(board[piece_row - 1][piece_col] == "_") :
				all_move.append(-2)
		
		# check move to right
		if(piece_col + 1 <= 2) :
			if(board[piece_row][piece_col + 1] == "_") :
				all_move.append(1)
		
		# check move to down
		if(piece_row + 1 <= 2) :
			if(board[piece_row + 1][piece_col] == "_") :
				all_move.append(2)
		
		# check diagonal move
		if(piece_col % 2 == piece_row % 2):

			# check up left
			if(piece_col - 1 >= 0 and piece_row - 1 >= 0) :
				if(board[piece_row - 1][piece_col - 1] == "_") :
					all_move.append(-3)
			
			# check up right
			if(piece_col + 1 <= 2 and piece_row - 1 >= 0) :
				if(board[piece_row - 1][piece_col + 1] == "_") :
					all_move.append(-4)
			
			# check down right
			if(piece_col + 1 <= 2 and piece_row + 1 <= 2) :
				if(board[piece_row + 1][piece_col + 1] == "_") :
					all_move.append(3)
			
			# check down left
			if(piece_col - 1 >= 0 and piece_row + 1 <= 2) :
				if(board[piece_row + 1][piece_col - 1] == "_") :
					all_move.append(4)

	return all_move

def make_move(board, prow, pcol, move_code, piece, pdefault) :
	match move_code :
		case -1 :
			board[prow][pcol] = pdefault
			board[prow][pcol - 1] = piece
		
		case 1 :
			board[prow][pcol] = pdefault
			board[prow][pcol + 1] = piece
		
		case -2 :
			board[prow][pcol] = pdefault
			board[prow - 1][pcol] = piece
		
		case 2 :
			board[prow][pcol] = pdefault
			board[prow + 1][pcol] = piece
		
		case -3 :
			board[prow][pcol] = pdefault
			board[prow - 1][pcol - 1] = piece
		
		case 3 :
			board[prow][pcol] = pdefault
			board[prow + 1][pcol + 1] = piece
		
		case -4 :
			board[prow][pcol] = pdefault
			board[prow - 1][pcol + 1] = piece

		case -4 :
			board[prow][pcol] = pdefault
			board[prow + 1][pcol - 1] = piece
	
	return board

def evaluate_board(b, depth) : 
	
	# Checking for Rows for X or O victory. 
	for row in range(3) :	 
		if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :		 
			if (b[row][0] == player_p) : 
				return -10 + depth
			elif (b[row][0] == opponent_p) : 
				return 10 - depth

	# Checking for Columns for X or O victory. 
	for col in range(3) : 
	
		if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) : 
		
			if (b[0][col] == player_p) : 
				return -10 + depth
			elif (b[0][col] == opponent_p) : 
				return 10 - depth

	# Checking for Diagonals for X or O victory. 
	if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) : 
	
		if (b[0][0] == player_p) : 
			return -10 + depth
		elif (b[0][0] == opponent_p) : 
			return 10 - depth

	if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) : 
	
		if (b[0][2] == player_p) : 
			return -10 + depth
		elif (b[0][2] == opponent_p) : 
			return 10 - depth

	# Else if none of them have won then return 0 
	return 0

def minimax(board, depth, isMax, prevPMove, prevOMove, max_depth) : 
	score = evaluate_board(board, depth)

	if(depth == max_depth) :
		return 0 

	# If Maximizer has won the game return his/her 
	# evaluated score 
	if (score == 10 - depth) : 
		return score 

	# If Minimizer has won the game return his/her 
	# evaluated score 
	if (score == -10 + depth) : 
		return score

	# If this maximizer's move 
	if (isMax) :	 
		best = -1000
		global oatt
		oatt = oatt + 1

		# Traverse all cells 
		for i in range(3) :		 
			for j in range(3) : 
			
				# Check if cell have opponent piece 
				if (board[i][j] == opponent_p) : 
					
					# find all move
					all_move = find_move(board, i, j)
					random.shuffle(all_move)
					 
					for move in all_move :

						if(prevOMove[0] == i and prevOMove[1] == j and prevOMove[2] == - move) :
							continue
						
						# Make the move 
						board = make_move(board, i, j, move, opponent_p, "_")

						newOmove = (i, j, move)

						# Call minimax recursively and choose 
						# the maximum value 
						best = max(best, minimax(board, depth + 1, not isMax, prevPMove, newOmove, max_depth))
						# print("AI Move Code: ", move, ", Piece: ", i, j, ", value: ", best, ", depth: ", depth) 

						# Undo the move 
						board = make_move(board, i, j, move, "_", opponent_p)
		return best 

	# If this minimizer's move 
	else : 
		best = 1000
		global patt
		patt = patt + 1

		# Traverse all cells 
		list_i = [0, 1, 2]
		random.shuffle(list_i) 
		for i in list_i :
			list_j = [0, 1, 2]
			random.shuffle(list_j)	 
			for j in list_j : 
			
				# Check if cell have player piece
				if (board[i][j] == player_p) : 
					
					# find all move
					all_move = find_move(board, i, j)
					random.shuffle(all_move)

					for move in all_move :

						if(prevPMove[0] == i and prevPMove[1] == j and prevPMove[2] ==  - move) :
							continue

						# Make the move 
						board = make_move(board, i, j, move, player_p, "_")

						newPMove = (i, j, move)

						# Call minimax recursively and choose 
						# the maximum value 
						best = min(best, minimax(board, depth + 1, not isMax, newPMove, prevOMove, max_depth))
						# print("Player Move Code: ", move, ", Piece: ", i, j, ", value: ", best, ", depth: ", depth) 

						# Undo the move 
						board = make_move(board, i, j, move, "_", player_p)
		return best 

# This will return the best possible move for the player 
def findBestMove(board, max_depth) : 
	bestVal = -1000
	bestMove = (-1, -1, 2) 

	# Traverse all cells, evaluate minimax function for 
	# all empty cells. And return the cell with optimal 
	# value.
	list_i = [0, 1, 2]
	random.shuffle(list_i) 
	for i in list_i :
		list_j = [0, 1, 2]
		random.shuffle(list_j)	 
		for j in list_j : 
		
			# Check if cell has opponent piece 
			if (board[i][j] == opponent_p) : 
				
				# find all move
				all_move = find_move(board, i, j)
				random.shuffle(all_move)

				prevOMove = (i, j, 0)
				prevPMove = (0, 0, 0)

				for move in all_move :
					board = make_move(board, i, j, move, opponent_p, "_")

					# compute evaluation function for this move
					moveVal = minimax(board, 0, False, prevPMove, prevOMove, max_depth)

					# undo the move
					board = make_move(board, i, j, move, "_", opponent_p)

					if(moveVal > bestVal) :
						bestMove = (i, j, move)
						bestVal = moveVal

	return bestMove
