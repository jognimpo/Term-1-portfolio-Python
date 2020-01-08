#benjamin vielstich
#11/11/2019
#tic tac toe

import random

#Global Constants
X = "X"
O = "O"
EMPTY = " "
NUM_SQUARES = 9

#working
def intro():
    """ display game instructions """
    print(
        """
                Tic-Tac-Toe

                Instructions:
                Enter a number between 1 - 9

                1  |  2  |  3
                -----------
                4  |  5  |  6
                -----------
                7  |  8  |  9
                
                """
        )

#works
def new_board():
    board = []
    for i in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """display board on screen,"""
    print(str.format("""
                {0}  |  {1}  |  {2}
                -----------
                {3}  |  {4}  |  {5}
                -----------
                {6}  |  {7}  |  {8}
                """,board[0],board[1],board[2],
                    board[3],board[4],
                    board[5],board[6],
                    board[7],board[8]))

#work
def ask_yes_no(question):
    """ask a yes or no question. and give a one letter response back"""
    response = None
    while response not in ("y","n","yes","no"):
        response = input(question).lower()
    x = response[0]    
    return x

#work
def ask_number(question, low, high):
    response = None
    while response not in range(low,high):
        try:
            response = int(input(question))
        except:
            print("ok buddy that was the last straw put a number in right now or else")  
    return response

#working
def assign_piece():
    first = ask_yes_no("do want to go first")
    if first == "y":
        human = "X"
        comp = "O"
    else:
        human = "O"
        comp = "X"
    return human, comp

#working
def switch_turn(turn):
    if turn == "X":
        return O
    else:
        return X
    
#working
def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

#works
def player_move(board,human):
    moves = legal_moves(board)
    move = None
    while move not in moves:
        move = ask_number("what is your move between 1 and 9",1,10)-1
        if move not in moves:
            print("fool you think this is a game? your actions have altered the course of time")
    return move

def winner(board):
    WAYS_TO_WIN = ((0,1,2),
                          (3,4,5),
                          (6,7,8),
                          (0,3,6),
                          (1,4,7),
                          (2,5,8),
                          (0,4,8),
                          (2,4,6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

        if EMPTY not in board:
            return TIE

        return None

#works
def comp_turn(board, comp, human):
    copy_board = board[:]
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("I will take square number", end=" ")
    
    for move in legal_moves(board):
        copy_board[move] = comp
        if winner(copy_board) == comp:
            print(move)
            return move
        copy_board[move] = EMPTY
        
    for move in legal_moves(board):
        copy_board[move] = human
        if winner(copy_board) == human:
            print(move)
            return move
        copy_board[move] = EMPTY
        
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return(move)
    
        
board = new_board()
board[0] = X
board[1] = X
x = comp_turn(board,O,X)
print(x)
board[x] = O
display_board(board)







