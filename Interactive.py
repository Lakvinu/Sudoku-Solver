import tkinter
import time

window = tkinter.Tk()
window.title("Sudoku Solver by Lakvinu")
#window.geometry("1050x880")

def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

#window.configure(background= rgbtohex(40,94,145))
window.configure(background=rgbtohex(25,73,114))
window.resizable(0,0)

board_two = [[0 for i in range(9)] for j in range(9)]

board = [[0 for i in range(9)] for j in range(9)]

with_slow = True
with_clear = False
has_started = False


def empty_pos():

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j

    return None, None

cnt = 0
def sudoku_solver():
    global board_two
    global cnt
    cnt += 1
    row, col = empty_pos()

    if row == None or col == None:
        return True

    for i in range(1, 10):
        if with_clear:
            return True

        set_text(row, col, i)

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
                if not has_started:
                    return row, i
                return False

    #checking within cols

    for i in range(9):
        if i != row:
            if board[i][col] == num:
                if not has_started:
                    return i, col
                return False

    #need to check within the current box

    #finding the start of the box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if i != row and j != col:
                if board[i][j] == num:
                    if not has_started:
                        return i, j
                    return False

    #if no mistakes return True

    return True


def begin():

    global board
    global with_clear
    global with_slow
    global has_started

    fast['state'] = 'active'

    """
    for i in range(9):
        for j in range(9):
            cur = board_two[i][j].get()
            if cur != '':
                board[i][j] = int(cur)
    """
    if has_started:
        return

    has_started = True
    with_clear = False
    with_slow = True
    start['state'] = 'disabled'
    sudoku_solver()


def erase():
    global board_two
    global with_clear
    global has_started

    fast['state'] = 'disabled'
    start['state'] = 'active'

    with_clear = True
    has_started = False

    for i in range(9):
        for j in range(9):
            board_two[i][j].delete(0, "end")
            board_two[i][j].insert(0, '')
            board[i][j] = 0


def instant():
    global with_slow
    global has_started
    fast['state'] = 'disabled'
    with_slow = False

def set_text(row, col, number):

    board_two[row][col].delete(0, "end")
    board_two[row][col].insert(0, str(number))

    if with_slow:
        window.update()
        time.sleep(0.0001)

def check_place(i,j,num):
    board[i][j] = num
    ans = is_valid(i,j,num)

    if ans == True:
        board_two[i][j]['bg'] = 'light green'
    else:
        board_two[i][j]['bg'] = 'red'
        board_two[ans[0]][ans[1]]['bg'] = 'red'
        window.update()
        time.sleep(0.4)
        board_two[ans[0]][ans[1]]['bg'] = 'light green'

def next_check(i,j):

    board_two[i][j]['bg'] = "white"
    num = board[i][j]
    board[i][j] = 0
    ans = is_valid(i, j, num)

    if ans != True:
        board_two[ans[0]][ans[1]]['bg'] = 'light green'

def validate(P,i,j):

    if len(P) == 0:
        # empty Entry is ok
        if not has_started:
            next_check(int(i),int(j))

        return True

    elif len(P) == 1 and P.isdigit():
        # Entry with 1 digit is ok
        if not has_started:
            check_place(int(i),int(j),int(P))

        return True

    else:
        # Anything else, reject it
        return False

vcmd = window.register(validate)

#build the layout
for i in range(9):
    for j in range(9):
        left, right = 0,0
        top, bottom = 0,0
        border_check = {2,5}

        if i in border_check:
            bottom = 5

        if j in border_check:
            right = 5

        box = tkinter.Entry(window, width=2, font=('Arial', 60), bd=1, highlightbackground = rgbtohex(170,38,54), highlightthickness=1, justify = "center", validate="key", validatecommand=(vcmd,'%P',i,j))
        box.grid(row=i, column=j, padx = (left, right), pady =(top, bottom))
        board_two[i][j] = box

start = tkinter.Button(window, height=1, width=7, text="Start", font=("Arial", 30), command=begin, bg="white")

fast = tkinter.Button(window, height=1, width=7, text="Fast", font=("Arial", 30), command=instant, bg="white", state="disabled")

clear = tkinter.Button(window, height=1, width=7, text="Clear", font=("Arial", 30), command=erase, bg="white")

start.grid(row=3, column=9, padx = 10)

clear.grid(row=5, column=9)

fast.grid(row=4, column=9)

#end of layout
window.mainloop()
