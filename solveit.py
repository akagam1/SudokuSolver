import pygame
from ui import *
import time

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

			#Update the board immediately with valid number
			"""numDisplay = font.render(str(i), False, (0, 0, 0), (250, 250, 250))
			screen.blit(numDisplay, (20 + column * 80, 20 + row * 80))
			pygame.display.update()"""


			if solution(board):
				return True
			
			board[row][column] = 0
			"""numDisplay = blank.render("", False, (0, 0, 0), (250, 250, 250))
			screen.blit(numDisplay, (20 + column * 80, 20 + row * 80))
			pygame.display.update()"""


	return False

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







		
	













