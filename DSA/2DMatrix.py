# 2D List or Matrix
# nums = [
#     [5, 20, 3],    # row 0
#     [7, -10, 9],   # row 1
#     [1, -52, 6]    # row 2
# ]

# # Accessing rows and columns
# rows = len(nums)       # number of rows = 3
# cols = len(nums[0])    # number of columns = 3

# for i in range(rows):
#     for j in range(cols):
#         print(nums[i][j])
# Index notation for 2D matrix
# nums[row][col] => nums[i][j]
# Example of indices:
# nums[0][0] = 5
# nums[0][1] = 20
# nums[0][2] = 3
# nums[1][0] = 7
# nums[1][1] = -10
# nums[1][2] = 9
# nums[2][0] = 1
# nums[2][1] = -52
# nums[2][2] = 6


# Transpose
# nums = [
#     [5, 9, 1],
#     [2, 3, 7]
# ]

# rows = len(nums)        # 2
# cols = len(nums[0])     # 3

# # Create empty transpose matrix
# result = [[0] * rows for _ in range(cols)]

# # Fill transpose
# for i in range(rows):
#     for j in range(cols):
#         result[j][i] = nums[i][j]

# print(result)


###########################################
# SET MATRIX ZEROS
###########################################

# Problem:
# If any element in the matrix is 0, set its entire row and column to 0.

# matrix = [[5, 20, 3],
#           [7, 0, 9],
#           [1, 0, 6],
#           [1, 0, 6],
#           [0, 3, 5]]  # Example input


# def setMatrix(matrix):
#     r = len(matrix)        # number of rows
#     c = len(matrix[0])     # number of columns


#     rowtrack = [0 for _ in range(r)]
#     coltrack = [0 for _ in range(c)]


#     for i in range(0, r):
#         for j in range(0, c):
#             if matrix[i][j] == 0:
#                 rowtrack[i] = -1
#                 coltrack[j] = -1

#     # Step 2: Update matrix
#     for i in range(0, r):
#         for j in range(0, c):
#             if rowtrack[i] == -1 or coltrack[j] == -1:
#                 matrix[i][j] = 0

#     return matrix


# print(setMatrix(matrix))

# Time Complexity  : O(N * M)   -> We scan the matrix twice
# Space Complexity : O(N + M)   -> Extra arrays rowtrack + coltrack

# Expected Output:
# [[0, 0, 3],
#  [0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]


##########################################
#90° CLOCKWISE ROTATION
##########################################

# Problem:
# Rotate the matrix by 90 degrees clockwise.
# from typing import List
# matrix = [[5, 20, 3],
#           [7, 0, 9],
#           [1, 0, 6]]  # Example input

# # Expected Output:
# # [
# #  [1, 7, 5],
# #  [0, 0, 20],
# #  [6, 9, 3]
# # ]

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)

#     # transpose
#         for i in range(n):
#          for j in range(i + 1, n):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#     #   reverse each row
#         for i in range(n):
#          matrix[i].reverse()
# # Time Complexity: O(n^2)
# #Space Complexity: O(1)  (in-place, no extra matrix)