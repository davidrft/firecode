# Let's have some fun with 2D Matrices! Write a method find_spiral to traverse a 2D matrix
# (List of Lists) of ints in a clockwise spiral order and append the elements to an output
# List of Integers.

# Example:

# Input Matrix :      
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# Output List:[1, 2, 3, 6, 9, 8, 7, 4, 5]

from typing import List

def find_spiral(matrix: List[List]) -> List[List]:

    # Rows
    top_row, bottom_row = 0, len(matrix)

    #Columns
    left_column, right_column = 0, len(matrix[0])

    spiral = []

    while top_row < bottom_row and left_column < right_column:
        for i in range(left_column, right_column):
            spiral.append(matrix[top_row][i])
        top_row += 1

        for i in range(top_row, bottom_row):
            spiral.append(matrix[i][right_column - 1])
        right_column -= 1

        if top_row < bottom_row:
            for i in range(right_column - 1, left_column-1, -1):
                spiral.append(matrix[bottom_row - 1][i])
            bottom_row -= 1
        
        if left_column < right_column:
            for i in range(bottom_row - 1, top_row - 1, -1):
                spiral.append(matrix[i][left_column])
            left_column += 1
    
    return spiral

if __name__ == '__main__':
    spiral = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(find_spiral(spiral))
    assert(find_spiral(spiral) == [1, 2, 3, 6, 9, 8, 7, 4, 5])