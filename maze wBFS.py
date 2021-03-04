import copy
from collections import deque
H, W = list(map(int,input().split()))
board = [list(input()) for i in range(H)]

check = False
for i in range(H):
    for j in range(W):
        if board[i][j] != '.':
            check = True


if check == False:
    print(H + W - 2)
    exit()

def bfs(y, x):

    bo = copy.deepcopy(board)

    moves = [(1,0), (-1,0), (0,1), (0,- 1)]

    maximum = 0

    myde = deque([(y, x, 0)])

    y_possible = set(list(range(H)))
    x_possible = set(list(range(W)))

    while myde:

        row, col, move = myde.popleft()

        bo[row][col] = '1'

        maximum = max(maximum, move)

        for i in range(4):

            y, x = moves[i]

            new_y, new_x = row + y,  col + x

            if new_y in y_possible and new_x in x_possible:

                if bo[new_y][new_x] == '.':
                    myde.append((new_y, new_x, move + 1))

    return maximum

max_val = 0
for y in range(H):
    for x in range(W):
        if board[y][x] == '.':
            max_val = max(bfs(y, x), max_val)

print(max_val)