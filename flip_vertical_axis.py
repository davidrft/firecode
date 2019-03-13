# You are given an m x n 2D image matrix (List of Lists) where each integer
# represents a pixel. Flip it in-place along its vertical axis.

# Example:
# Input image :
# 1 0              
# 1 0

# Modified to :
# 0 1              
# 0 1

from typing import List

def flip_vertical_axis(matrix: List[List]):
    for i in range(len(matrix)):
        for j in range(len(matrix[0]) // 2):
            matrix[i][j], matrix[i][~j] = matrix[i][~j], matrix[i][j]
