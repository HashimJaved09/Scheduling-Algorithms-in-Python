import os
import sys
import random

BLACK = "\033[0;30m"
RED = "\033[1;31m"
GREEN = "\033[0;32m"  
ORANGE = "\033[0;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[0;35m"
CYAN = "\033[1;36m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

def tictactoe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
    	sys.stdout.write(REVERSE)
    	print '\t\t-------------'
        print '\t\t|', board[0], '|', board[1], '|', board[2], '|'
        print '\t\t|', board[3], '|', board[4], '|', board[5], '|'
        print '\t\t|', board[6], '|', board[7], '|', board[8], '|'
        print '\t\t-------------'

    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p1()
        else:
            board[n] = "X"

    def p2():
        while True:
            n = random.randint(0, 8)
            if board[n] == n + 1:
                board[n] = "O"
                break
            else:
                continue   

    def choose_number():
        while True:
            a = input()
            a -= 1
            if a in range(0, 9):
                return a
            else:
                print("\nThat's not on the board. Try again")
                continue

    def check_board():
    	sys.stdout.write(BLUE)
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Player 1 Wins!\n")
                print("Congratulations!\n")
                return True
            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Computer Wins!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True
    
    while not end:
    	sys.stdout.write(GREEN)
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 1 choose where to place a cross")
        p1()
  
        draw()
        end = check_board()
        if end == True:
            break
        print("Computer's Turn with nought")
        p2()

os.system('clear')
while True:
	os.system('clear')
	tictactoe()
	sys.stdout.write(RED)
	if input("Play again (1/0)\n") == 1:
		continue
	break
