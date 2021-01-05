# SudokuSolver
## BasicSudokuSolver.py
This scipt has as input a two dimensional array that keeps the sudoku cells. 
```python
sudoku = [[1, 0, 0, 0, 9, 0, 6, 0, 8,], 
          [0, 0, 6, 0, 1, 0, 0, 4, 2,],
          [0, 7, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0, 0, 3, 0, 7, 0, 1,],
          [0, 9, 0, 0, 7, 0, 0, 5, 0,],
          [8, 0, 0, 0, 0, 0, 0, 6, 0,],
          [3, 0, 0, 0, 0, 6, 5, 0, 0,],
          [0, 0, 5, 0, 4, 1, 2, 0, 7,],
          [0, 0, 0, 5, 0, 9, 0, 0, 0 ]] 
```

0 means that this cell is empty.
Then after the solution is printed is the terminal like:
``` python 
1  2  3  4  9  5  6  7  8 
9  5  6  8  1  7  3  4  2 
4  7  8  2  6  3  9  1  5 
5  6  4  9  3  8  7  2  1 
2  9  1  6  7  4  8  5  3 
8  3  7  1  5  2  4  6  9 
3  1  9  7  2  6  5  8  4 
6  8  5  3  4  1  2  9  7 
7  4  2  5  8  9  1  3  6 
```

## Sudoku Online.py
This script reads a sudoku from the site https://www.livesudoku.com/ and then it insert it writes it in the form a two dimendional array. Then it solves this array and uses numpad and arrow keys in order to solve the sudoku in the website.
