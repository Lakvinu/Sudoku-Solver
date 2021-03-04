import numpy as np


def sudoku_solver():

    # finding the next empty spot
    not_Found = True

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                row, col = i, j
                not_Found = False
                break

        else:
            continue

        break

    # checking all positions are filled hence
    # if not_found == True; finished
    if not_Found == True:
        return True


    for i in range(1, 10):



        if is_valid(row, col, i) == True:

            board[row][col] = i

            #if current number works

            if sudoku_solver() == True:
                return True

            #if current number fails

            else:

                board[row][col] = 0

    return False





def is_valid(row, col, num):

    #checking within rows

    for i in range(9):
        if i != col:
            if board[row][i] == num:
                return False

    #checking within cols

    for i in range(9):
        if i != row:
            if board[i][col] == num:
                return False

    #need to check within the current box

    #finding the start of the box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if i != row and j != col:
                if board[i][j] == num:
                    return False

    #if no mistakes return True

    return True





board = np.array([
[4, 0, 0, 0, 0, 5, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 9, 8],
[3, 0, 0, 0, 8, 2, 4, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 8, 0],
[9, 0, 3, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 3, 0, 6, 7, 0],
[0, 5, 0, 0, 0, 9, 0, 0, 0],
[0, 0, 0, 2, 0, 0, 9, 0, 7],
[6, 4, 0, 3, 0, 0, 0, 0, 0],
])



sudoku_solver()

print(board)
