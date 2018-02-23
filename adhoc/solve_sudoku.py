# Solved using Back tracking and Exhaustive Method.
# It take a lot of time in case solution doesn't exists

#!/bin/python
def find_next_empty_slot(grid, free_slot):
  i_start = free_slot[0]
  j_start = free_slot[1]
  for i in xrange(i_start, 9):
    if i != i_start:
      j_start = 0
    for j in range(j_start, 9):
      if not grid[i][j]:
        free_slot[0], free_slot[1] = i, j
        return True
  return False

def used_in_row(grid, l ,value):
  row = l[0]
  for col in range(9):
    if value == grid[row][col]:
      return True
  return False

def used_in_col(grid, l, value):
  col = l[1]
  for row in range(9):
    if grid[row][col] == value:
      return True
  return False

def used_in_box(grid, l, value):
  row_start = 3*(l[0]/3)
  col_start = 3*(l[1]/3)

  for i in range(3):
    for j in range(3):
      row, col = row_start+i, col_start+j
      if value == grid[row][col]:
        return True
  return False

def is_feasible(grid, l, value):
  return not used_in_row(grid, l, value) and not used_in_col(grid, l, value) and \
    not used_in_box(grid, l, value)


def solve(grid, start_i, start_j):
  free_slot = [start_i, start_j]
  if not find_next_empty_slot(grid, free_slot):
    return True

  for i in range(1, 10):
    if is_feasible(grid, free_slot, i):
      grid[free_slot[0]][free_slot[1]] = i
      if solve(grid, *free_slot):
        return True
      grid[free_slot[0]][free_slot[1]] = 0

  return False


def print_grid(grid):
  for i in range(9):
    col_val = []
    for j in range(9):
      col_val.append(str(grid[i][j]))
    print " ".join(col_val)

N = int(raw_input())
grid = []
for _ in range(N):
  for _ in range(9):
    row = raw_input()
    row = map(int, row.split(" "))
    grid.append(row)
  solve(grid, 0, 0)
  print_grid(grid)

