import cv2
import pytesseract
import numpy as np
import pyautogui
import time

time.sleep(2)
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]  # empty array in start


LeftUpCorner = [731, 152] # set Coordinates for the top Right 
RightBottomCorner = [1125, 537]
xCellSize = (RightBottomCorner[0] - LeftUpCorner[0]) / 9
yCellSize = (RightBottomCorner[1] - LeftUpCorner[1]) / 9

e = 5 # crop each side by e pixels
for i in range(9):
    for j in range(9):
        digit = image[int(LeftUpCorner[1]+j*yCellSize+e):int(LeftUpCorner[1]+(j+1)*yCellSize-e), int(LeftUpCorner[0]+i*xCellSize+e):int(LeftUpCorner[0]+(i+1)*xCellSize - e)]  # get each digit
        cv2.imwrite("Desktop/sudoku/png/img"+str(j)+str(i)+".png", digit)  # save as a new photo

def isint(s):  # check if the character in the cell is number
    try:
        int(s)
        return True
    except ValueError:
        return False


def valid(x, y, n):  # check if number n can go in the cell (x,y)
    for i in range(9):  # check row
        if(sudoku[x][i] == n):
            return False
    for i in range(9):  # check column
        if(sudoku[i][y] == n):
            return False
    for i in range(3):  # check 3*3 box
        for j in range(3):
            if(sudoku[(x//3)*3+i][(y//3)*3+j] == n):
                return False
    return True


def solve():   # solve sudoku
    global sudoku
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:  # check if it is empty
                for n in range(9):
                    if valid(x, y, n+1):  # check if the n is valid in the empty cell
                        sudoku[x][y] = n+1
                        solve()  # start a new solution with n in the empty cell
                        sudoku[x][y] = 0  # remove the number again
                return
    for r in sudoku:
        for c in r:
            print(c, end=" ")  # print Solved Sudoku
        print()
    print()
    print()
    print()
    input("go?")
    time.sleep(2)
    for i in range(9):
        for j in range(9):  # write results back to the website
            if i != 0 or j != 0:
                pyautogui.press('right')
            pyautogui.write(str(sudoku[i][j]))
            #time.sleep(2)


for i in range(9):
    for j in range(9):
        # read the previously saved images
        image = cv2.imread("Desktop/sudoku/png/img"+str(i)+str(j)+".png")
        out_below = pytesseract.image_to_string(
            image, config='--psm 6')  # read the number of the image
        if isint(out_below):  # check if it is number
            sudoku[i][j] = int(out_below)  # add it to sudoku
        else:
            sudoku[i][j] = 0  # The cell is empty so value equals 0

for r in sudoku:  # print the read sudoku
    for c in r:
        print(c, end=" ")
    print()
print()
print()

solve()
