def check_validity(puzzle, i_check = [], j_check = []):
    ''' Given a puzzle, returns if the puzzle is in a valid state.
    
    if i and j are given, it only checks the validity of that square in the puzzle'''

    # check if rows, columns are valid
    for i in range(9):
        row = [False]*9
        col = [False]*9
        # check rows
        for j in range(9):
            if puzzle[i][j]-1 < 0 :
                continue
            elif row[puzzle[i][j]-1] == False:
                row[puzzle[i][j]-1] = True
            else:
                return False
        #check cols
        for j in range(9):
            if puzzle[j][i]-1 < 0 :
                continue
            elif col[puzzle[j][i]-1] == False:
                col[puzzle[j][i]-1] = True
            else:
                return False
        #check square
        for j in range(9):
            pass
    return True
    
def solver(puzzle):
    ''' Solves sudoku puzzle using brute force search.

    <puzzle> is a 9x9 matrix.
    Blank squares are indicated with zeros'''

    # Check each square withouth a number
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] > 0:
                continue
            else:
                for guess in range(1, 10):
                    new_puzzle = [x[:] for x in puzzle]
                    new_puzzle[i][j] = guess
                    if check_validity(new_puzzle):
                        puzzle = solver(new_puzzle)
                        break
                    else:
                        continue
    return puzzle

valid_puzzle = [[3, 9, 1, 2, 8, 6, 5, 7, 4],\
    [4, 8, 7, 3, 5, 9, 1, 2, 6],\
    [6, 5, 2, 7, 1, 4, 8, 3, 9],\
    [8, 7, 5, 4, 3, 1, 6, 9, 2],\
    [2, 1, 3, 9, 6, 7, 4, 8, 5],\
    [9, 6, 4, 5, 2, 8, 7, 1, 3],\
    [1, 4, 9, 6, 7, 3, 2, 5, 8],\
    [5, 3, 8, 1, 4, 2, 9, 6, 7],\
    [7, 2, 6, 8, 9, 5, 3, 4, 1]]

invalid_puzzle = [[3, 3, 1, 2, 8, 6, 5, 7, 4],\
    [4, 8, 7, 3, 5, 9, 1, 2, 6],\
    [6, 5, 2, 7, 1, 4, 8, 3, 9],\
    [8, 7, 5, 4, 3, 1, 6, 9, 2],\
    [2, 1, 3, 9, 6, 7, 4, 8, 5],\
    [9, 6, 4, 5, 2, 8, 7, 1, 3],\
    [1, 4, 9, 6, 7, 3, 2, 5, 8],\
    [5, 3, 8, 1, 4, 2, 9, 6, 7],\
    [7, 2, 6, 8, 9, 5, 3, 4, 1]] 

invalid_puzzle_col = [[3, 9, 1, 2, 8, 6, 5, 7, 4],\
    [3, 8, 7, 3, 5, 9, 1, 2, 6],\
    [6, 5, 2, 7, 1, 4, 8, 3, 9],\
    [8, 7, 5, 4, 3, 1, 6, 9, 2],\
    [2, 1, 3, 9, 6, 7, 4, 8, 5],\
    [9, 6, 4, 5, 2, 8, 7, 1, 3],\
    [1, 4, 9, 6, 7, 3, 2, 5, 8],\
    [5, 3, 8, 1, 4, 2, 9, 6, 7],\
    [7, 2, 6, 8, 9, 5, 3, 4, 1]] 

incomplete_puzzle = [[3, 0, 1, 2, 8, 6, 5, 7, 4],\
    [4, 8, 7, 3, 5, 9, 1, 2, 6],\
    [6, 5, 2, 7, 1, 4, 8, 3, 9],\
    [8, 7, 5, 4, 3, 1, 6, 9, 2],\
    [2, 1, 3, 9, 6, 7, 4, 8, 5],\
    [9, 6, 4, 5, 2, 8, 7, 1, 3],\
    [1, 4, 9, 6, 7, 3, 2, 5, 8],\
    [5, 3, 8, 1, 4, 2, 9, 6, 7],\
    [0, 2, 6, 8, 9, 5, 3, 4, 1]] 



# print(check_validity(valid_puzzle))
# print(check_validity(invalid_puzzle))
# print(check_validity(invalid_puzzle_col))
# print(check_validity(incomplete_puzzle))

last_square_missing = [[0, 9, 1, 2, 8, 6, 5, 7, 4],\
    [4, 8, 7, 3, 5, 9, 1, 2, 6],\
    [6, 5, 2, 7, 1, 4, 8, 3, 9],\
    [8, 7, 5, 4, 3, 1, 6, 9, 2],\
    [2, 1, 3, 9, 6, 7, 4, 8, 5],\
    [9, 6, 4, 5, 2, 8, 7, 1, 3],\
    [1, 4, 9, 6, 7, 3, 2, 5, 8],\
    [5, 3, 8, 1, 4, 2, 9, 6, 7],\
    [7, 2, 6, 8, 9, 5, 3, 4, 1]]

print(solver(last_square_missing))
print(solver(incomplete_puzzle))