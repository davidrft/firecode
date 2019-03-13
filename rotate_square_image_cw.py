# You are given a square 2D image matrix (List of Lists) where each integer
# represents a pixel. Write a method rotate_square_image_ccw to rotate the image
# counterclockwise - in-place. This problem can be broken down into simpler
# sub-problems you've already solved earlier! Rotating an image counterclockwise
# can be achieved by taking the transpose of the image matrix and then flipping
# it on its horizontal axis.

# Example:
# Input image :      
# 1 0                          
# 1 0
# Modified to :       
# 0 0                          
# 1 1

from typing import List

def rotate_square_image_ccw(matrix: List[List]):
    def flip_horizontal_axis(M):
        for i in range(len(matrix) // 2):
            matrix[i], matrix[~i] = matrix[~i], matrix[i]
    
    def transpose(M):
        for i in range(0, len(M)):
            for j in range(i+1, len(M)):
                M[i][j], M[j][i] = M[j][i], M[i][j]
    
    transpose(matrix)
    flip_horizontal_axis(matrix)

if __name__ == '__main__':
    a = [[1, 0],
         [1, 0]]
    b = [[0, 0],
         [1, 1]]
    rotate_square_image_ccw(a)
    assert(a == b)