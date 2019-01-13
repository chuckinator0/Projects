'''
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, 
each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the 
layout rules described above. Note that the puzzle represented by grid does not have to be solvable.
'''


def sudoku2(grid):
    
    def check_duplicates(array):
        # return false if there is a duplicate, true otherwise
        s = set()
        for entry in array:
            if entry != '.' and entry in s:
                return False
            else:
                s.add(entry)
        return True
        
    
    # check each row for duplicates
    if not all([check_duplicates(row) for row in grid]):
        return False
    if not all([check_duplicates(column) for column in zip(*grid)]):
        return False
    
    # check the 9 3x3 subgrids
    def check_subgrid(m,n):
        s = set()
        for i in range(3*m,3+3*m):
            for j in range(3*n,3+3*n):
                if grid[i][j] != '.' and grid[i][j] in s:
                    return False
                else:
                    s.add(grid[i][j])
        return True
    
    for m in range(3):
        for n in range(3):
            if not check_subgrid(m,n):
                return False
    
    return True
