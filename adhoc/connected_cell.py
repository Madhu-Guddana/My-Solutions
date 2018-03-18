#!/bin/python

# Question:
# Given an  matrix, 
# find and print the number of cells in the largest region in the matrix. 
# Note that there may be more than one region in the matrix.

# Sources:
# 1. https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem
# 2. https://practice.geeksforgeeks.org/problems/find-the-number-of-islands


# Solution:
# Solution is using DFS.
# Given an array
# [1,0,0,1]
# [1,1,0,1]
# [0,0,1,0]
# [1,0,0,0]
# Go dept first search, mark everything that is visited,
# Maintain a count and you will arrive at answer.

import sys

def island_size(arr, i, j):
  if not(0 <= i < len(arr) and 0<= j < len(arr[0])):
    return 0
  
  # -1 indicates, node been visited.
  if arr[i][j] ==0 or arr[i][j] == -1:
    return 0

  count =1
  arr[i][j] = -1

  # Dept First Search.
  count += island_size(arr, i-1, j)
  count += island_size(arr, i-1, j-1)
  count+= island_size(arr, i-1, j+1)
  count+= island_size(arr, i+1, j)
  count += island_size(arr, i+1, j-1)
  count+= island_size(arr, i+1, j+1)
  count += island_size(arr, i, j-1)
  count+= island_size(arr, i, j+1)

  return count

def connectedCell(arr):
  if not arr:
    return 0
  n = len(arr)
  m = len(arr[0])
  max_count = 0
  for i in range(n):
    for j in range(m):
      max_count = max(max_count,island_size(arr, i, j))
  return max_count


if __name__ == "__main__":
    n = int(raw_input().strip())
    m = int(raw_input().strip())
    matrix = []
    for matrix_i in xrange(n):
        matrix_temp = map(int,raw_input().strip().split(' '))
        matrix.append(matrix_temp)
    result = connectedCell(matrix)
    print result
