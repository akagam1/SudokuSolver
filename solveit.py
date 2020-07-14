board1 = [[5,3,0,0,7,0,0,0,0],
		  [6,0,0,1,9,5,0,0,0],
		  [0,9,8,0,0,0,0,6,0],
		  [8,0,0,0,6,0,0,0,3],
		  [4,0,0,8,0,3,0,0,1],
		  [7,0,0,0,2,0,0,0,6],
		  [0,6,0,0,0,0,2,8,0],
		  [2,0,0,4,1,9,0,0,5],
		  [0,0,0,0,8,0,0,7,9]]

#define solve function that calls upon other functions
def solution(board):
	void = find_void(board)
	if not void:
		return True
	else: 
		row, column = void

	for i in range(1,10):
		if valid(board,i,(row,column)):
			board[row][column] = i
			
			if solution(board):
				return True
			
			board[row][column] = 0
	return False


#define function that prints the board in a presentable manner
def print_board(board):
	for i in range(len(board)):

		if i%3 == 0 and i != 0:
			print("- - - - - - - - - - - - - - - - - ")

		for j in range(len(board[0])):
			if j%3 == 0 and j != 0:
				print(' | ', end="")

			if j == 8:
				print(" "+ str(board[i][j]))
			else:
				print(" " + str(board[i][j]) + " ", end="")

#define function that finds empty spaces(**i=row and j=column**)
def find_void(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i,j)
	return None

#define function that checks if input value is valid=====>{note: cross check if value is unique for the row,column and the box}
def valid(board,num,position):
	for i in range(len(board[0])):
		if board[position[0]][i] == num and i != position[1]:
			return False

	for i in range(len(board)):
		if board[i][position[1]] == num and i != position[0]:
			return False

	y_block = position[0]//3  #mini 3x3 grid coordinates
	x_block = position[1]//3

	for i in range(y_block*3, y_block*3 + 3):
		for j in range(x_block*3, x_block*3 + 3):
			if board[i][j] == num and (i,j) != position:
				return False

	return True

"""print_board(board1)
solution(board1)
print("												")
print("- - - - - - - - - - - - - - -  - -  -  - - --")
print("												")
print_board(board1)"""





		
	













