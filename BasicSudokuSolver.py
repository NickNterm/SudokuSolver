sudoku = [[1, 0, 0, 0, 9, 0, 6, 0, 8,], # 0 means empty cell
          [0, 0, 6, 0, 1, 0, 0, 4, 2,],
          [0, 7, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0, 0, 3, 0, 7, 0, 1,],
          [0, 9, 0, 0, 7, 0, 0, 5, 0,],
          [8, 0, 0, 0, 0, 0, 0, 6, 0,],
          [3, 0, 0, 0, 0, 6, 5, 0, 0,],
          [0, 0, 5, 0, 4, 1, 2, 0, 7,],
          [0, 0, 0, 5, 0, 9, 0, 0, 0 ]] # sudoku example 

def valid(x, y, n): # check if number n can go in the cell (x,y)
    for i in range(9): # check row
        if(sudoku[x][i] == n):
            return False
    for i in range(9): # check column
        if(sudoku[i][y] == n):
            return False
    for i in range(3): # check 3*3 box
        for j in range(3):
            if(sudoku[(x//3)*3+i][(y//3)*3+j] == n):
                return False
    return True

def solve(): # solve sudoku
    global sudoku
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0: # check if it is empty
                for n in range(9):
                    if valid(x, y, n+1): # check if the n is valid in the empty cell
                        sudoku[x][y] = n+1
                        solve() # start a new solution with n in the empty cell
                        sudoku[x][y] = 0 # remove the number again
                return
    for r in sudoku:
        for c in r:
            print(c, end=" ")  # print Solved Sudoku
        print()
    print()
    print()
    print()

solve()