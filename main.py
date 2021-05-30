import numpy as np

#TODO: Create a board
board = np.zeros((3, 3)).astype(int)

# print(board)
turn = 1
move = 9


#TODO Check the winner
def check_win():
    if any(np.sum(board, 1)==3) or any(np.sum(board, 0)==3) or sum(np.diag(board))==3 or sum(np.diag(board)[::-1])==3:
        return True

    if any(np.sum(board, 1)==-3) or any(np.sum(board, 0)==-3) or sum(np.diag(board))==-3 or sum(np.diag(board)[::-1]==-3):
        return True

    return False


#TODO: Create players and move
def play_turn():
    global turn, move
    x = int(input(f"What is player {turn}'s X position?"))
    y = int(input(f"What is player {turn}'s Y position?"))
    try:
        if board[y, x]==0:
            board[y, x]=turn
        else:
            play_turn()
    except IndexError:
        play_turn()
        if check_win():
            print(f"Player {turn} has won!")

        turn = turn*-1
        move = move -1


#TODO GAME ON COMANDLINE

while move > 0:
    print (board)
    play_turn()

