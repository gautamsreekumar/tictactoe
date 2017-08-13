from numpy import *
from os import *

def markPosition(canvas, playername, n):
    moves = int(raw_input("Enter position "))
    x = int(moves/10)-1
    y = int(moves%10)-1
    if x > n-1 or y > n-1:
        print "Invalid position"
        temp = markPosition(canvas, playername, n)
    elif canvas[x, y] == 2*n:
        canvas[x, y] = playername
        temp = canvas
    else:
        print "Position occupied"
        temp = markPosition(canvas, playername, n)
    return temp

def displayCanvas(canvas, n):
    system('clear')
    print "     1        2        3\n"
    for i in range(0, n):
        temp = ""
        for j in range(0, n):
            if (canvas[i, j] == 2*n):
                temp += '-        '
            elif (canvas[i, j] == 1):
                temp += 'x        '
            elif (canvas[i, j] == 2):
                temp += 'o        '
        print i+1, "  ", temp, "\n"

# this is a multiplayer version of tic tac toe

n = 3 # you can set the size of the canvas
canvas = 2*n*ones((n, n)) # this is the canvas that will be displayed
seals = ['x', 'o']

# the valid inputs are 1 and 2. 1 for x and 2 for o
# the player has mention the position using two digits
# such as 11, 12, 32, 23, etc.

# the indices of the columns are {1, 3} starting from top, while the indices of the rows are {1, 3} starting from left

print "Player 1's moves are shown as x and Player 2's moves are shown as o\n"
print "Enter the position for each move as numbers from 1 to 3"
print "For example, 12 means the move is on row 1 and column 2\n"
name = ["", ""]
name[0] = raw_input("Enter player 1's name ")
name[1] = raw_input("Enter player 2's name ")
print "Are you ready to begin? [press ENTER]"
raw_input()
            
# inputting moves in a loop  until someone wins
gameon = True
playername = 1
move_count = 0
while gameon and move_count < 9:
    displayCanvas(canvas, n)
    row_sum = sum(canvas, 1)
    column_sum = sum(canvas, 0)
    diagonal_sum = trace(canvas)
    adiagonal_sum = trace(fliplr(canvas))
    print "row_sum ", row_sum
    print "column_sum ", column_sum
    print "diagonal_sum ", diagonal_sum
    print "adiagonal_sum ", adiagonal_sum
    print name[playername-1], "'s move"
    print move_count
    print (2*n in column_sum)
    canvas = markPosition(canvas, playername, n)
    row_sum = sum(canvas, 1)
    column_sum = sum(canvas, 0)
    diagonal_sum = trace(canvas)
    adiagonal_sum = trace(fliplr(canvas))
    if (n in row_sum) or (n in column_sum) or diagonal_sum == n or adiagonal_sum == n:
        gameon = False
        displayCanvas(canvas, n)
        print name[0], " wins"
    elif (2*n in row_sum) or (2*n in column_sum) or diagonal_sum == 2*n or adiagonal_sum == 2*n:
        gameon = False
        displayCanvas(canvas, n)
        print name[1], " wins"
    else:
        playername = 3 - playername
        move_count += 1

if gameon:
    print "Draw"
