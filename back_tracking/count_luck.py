# Source: https://www.hackerrank.com/challenges/count-luck/problem

# Question:
# Consider the forest as an  grid N X M. Each cell is either empty(.) or
# blocked by a tree (x). A person can move LEFT, RIGHT, UP, and DOWN
# through empty cells but not via tree cells. His cur cell is marked with
# the character 'M' , and dest is marked  with '*' . The upper-left corner
# is indexed as [0][0].

# Assume there is only 1 way possible to reach destination.
# k is the estimated number of points where path splits.
# Print "Impressed" if estimation is correct, "Oops!" otherwise.


#!/bin/python3

import sys

def get_available_paths(matrix, pos):
  r = pos[0]
  c = pos[1]
  neigh = [       (r-1, c),
           (r, c-1),     (r, c+1),
                  (r+1, c)]
  ret_val = []
  for ele in neigh:
    i,j = ele[0], ele[1]
    if 0<=i<len(matrix) and 0<=j<len(matrix[i]):
      if matrix[i][j]== '.' or matrix[i][j]== '*':
        ret_val.append((i,j))
  return ret_val


def traverse(matrix, pos, count):
  if matrix[pos[0]][pos[1]] == '*':
    return count
  matrix[pos[0]][pos[1]] = 'V' # Visited
  paths = get_available_paths(matrix, pos)

  if len(paths) > 1:
    count+=1
  for path in paths:
    ret_val = traverse(matrix, path, count)
    if ret_val!= -1:
      return  ret_val
  return -1

def countLuck(matrix, k):
  source =[(i,j) for i in range(len(matrix)) for j in range(len(matrix[i]))
           if matrix[i][j] == 'M']
  source = source[0]
  ans = traverse(matrix, source, 0)
  if ans == k:
    return 'Impressed'
  else:
    return 'Oops!'

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in range(t):
        n, m = raw_input().strip().split(' ')
        n, m = [int(n), int(m)]
        matrix = []
        matrix_i = 0
        for matrix_i in range(n):
           matrix_t = str(raw_input()).strip()
           matrix.append([char for char in matrix_t])
        k = int(raw_input())
        result = countLuck(matrix, k)
        print(result)




