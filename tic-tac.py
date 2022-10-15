#Tic Tac Toe game in python
from random import *
from time import sleep

board = [" " for i in range(10)]

def insert_letter(letter, pos):
    board[pos] = letter

def space_is_free(pos) -> bool:
    return board[pos] == " "

def print_board(board):
    print('   |   |')
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print('   |   |')
    print("-" * 11)
    print('   |   |')
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print('   |   |')
    print("-" * 11)
    print('   |   |')
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print('   |   |')


def is_winner(bo, le):
    return (
    (bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[3] == le and bo[6] == le and bo[9] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le)
    )

def player_move():
    run: bool = True

    while run:
        move = input('Please enter the position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if 0< move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter("X", move)
                else:
                    print('Sorry, the space has been occupied')
            else:
                print('Please type a number within the range (1-9)')

        except:
            print('Please enter a number!')

def comp_move():
    pos_moves = [x for x, c in enumerate(board) if c == " " and x != 0]
    move = 0

    for let in ["O", "X"]:
        for i in pos_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move
    corners_open = []
    for i in pos_moves:
        if i in [1,3,7,9,5]:
            corners_open.append(i)
    if corners_open != []:
        move = select_random(corners_open)
        return move
    return move

def select_random(board):
    move = choice(board)
    return move

def is_board_full(board):
    return board.count(" ") <= 1

def main():
    print("Welcome to Tic Tac Toe! game")
    print_board(board)

    while not is_board_full(board):
        if not is_winner(board, "O"):
            player_move()
            print_board(board)
        else:
            print("Sorry, O\'s won the game")
            print("Starting again....")
            exit()


        if not is_winner(board, "X"):
            move = comp_move()
            if move == 0:
                print("Tie Game!")
                return 0

            else:
                insert_letter("O", move)
                print(f"Computer placed an \'O\' in position {move}")
                print_board(board)

        else:
            print("Hurray!, X\'s won the game, Good job")
            print("Starting again....")
            exit()

    if is_board_full(board):
        print("Tie Game!")


if __name__ == "__main__":
    while True:
        main()
