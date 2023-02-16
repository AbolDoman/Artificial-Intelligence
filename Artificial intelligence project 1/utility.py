RED     = '\033[1;31;40m'
YELLOW  = '\033[1;33;40m'
BLUE    = '\033[1;34;40m'
MAGENTA = '\033[1;35;40m'
CYAN    = '\033[1;36;40m'
WHITE   = '\033[1;37;40m'
AI_PLAYER = 1
HUMAN_PLAYER = 0
BOARD_HEIGHT = 6
BOARD_WIDTH = 7

def utilityValue(board, piece):
    	# Check horizontal locations for win
	for c in range(BOARD_WIDTH-3):
		for r in range(BOARD_HEIGHT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(BOARD_WIDTH):
		for r in range(BOARD_HEIGHT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(BOARD_WIDTH-3):
		for r in range(BOARD_HEIGHT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(BOARD_WIDTH-3):
		for r in range(3, BOARD_HEIGHT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def get_valid_locations(board):
    valid_locations = []
    for col in range(BOARD_WIDTH):
        if utilityValue(board, col):
            valid_locations.append(col)
    return valid_locations
      

def gameIsOver(board):
	return utilityValue(board, HUMAN_PLAYER) or utilityValue(board, AI_PLAYER) or len(get_valid_locations(board)) == 0