player_p = 'O'
opponent_p = 'X'

def isOnWin(b):
    # Checking for Rows for X or O victory. 
	for row in range(3) :	 
		if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :		 
			if (b[row][0] == player_p) or (b[row][0] == opponent_p):
				return True

	# Checking for Columns for X or O victory. 
	for col in range(3) : 
		if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) : 
			if (b[0][col] == player_p) or (b[0][col] == opponent_p):
				return True

	# Checking for Diagonals for X or O victory. 
	if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) : 
	
		if (b[0][0] == player_p) or (b[0][0] == opponent_p): 
			return True

	if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) : 
	
		if (b[0][2] == player_p) or (b[0][2] == opponent_p): 
			return True

	# Else if none of them have won then return 0 
	return False