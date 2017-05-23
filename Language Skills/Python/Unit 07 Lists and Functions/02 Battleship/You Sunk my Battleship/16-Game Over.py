from random import randint

board = []
numberTurns = [0,1,2,3]
guess_row = 0
guess_col = 0
for x in range(0, 8):
    board.append(["O"] * 8)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print ship_row
print ship_col

for turn in numberTurns:
    print "Turn", turn + 1
    while guess_row == 0:
        try:
            guess_row = int(raw_input("Guess Row:"))
        except ValueError:
            print "Nothing entered... try again"

    while guess_col == 0:
        try:
            guess_col = int(raw_input("Guess Col:"))
        except ValueError:
            print "Nothing entered... try again"

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"
        break
    else:
        if (guess_row > len(board) or guess_row < 0 ) or (guess_col > len(board) or guess_col < 0 ):
            print "Oops, that's not even in the ocean."
        elif board[int(guess_row)][int(guess_col)] == "X":
            print "You guessed that one already."
            if turn < len(numberTurns):
                chances = (len(numberTurns) - 1) - turn
                print "Chances left: %s" % chances
            elif turn == len(numberTurns):
                print "No more chances. Game Over"
                break
        else:
            print "You missed my battleship!"
            board[int(guess_row)][int(guess_col)] = "X"
            if turn < len(numberTurns):
                chances = (len(numberTurns) - 1) - turn
                print "Chances left: %s" % chances
            elif turn == len(numberTurns):
                print "No more chances. Game Over"
                break
        print_board(board)  
        guess_row = 0
        guess_col = 0
if turn == 3:
    print "Game Over"
