# This was very intersting problem.

# Question:
# Given a list of building heights in order from left to right, assuming the buildings are adjacent, 
# calculate the largest rectangle you could form choosing any segment of the line of buildings.

# Clue for O(n) solution:
# Idea here is to have l_index and r_index for cur_index, which gives area covered by building at 
# index completely included in the area calculation.

# Sources:
# 1) https://www.hackerrank.com/challenges/largest-rectangle/problem
# 2) https://www.geeksforgeeks.org/largest-rectangle-under-histogram/


#!/bin/python

import sys

def calculate_area(areas,stack, r_index):
    top_ele = stack.pop()
    t_index, t_item = top_ele[0], top_ele[1]
    l_index = stack[-1][0] if stack else -1
    area = t_item*(r_index-l_index-1)
    areas[t_index] = area

def largestRectangle(h):
    stack = []
    if not h:
      return 0
    stack.append((0,h[0]))
    areas = [0]*len(h)
    for index in range(1,len(h)):
      item = h[index]
      while stack and item < stack[-1][1]:
        calculate_area(areas, stack, index)
      stack.append((index, item))
    
    # Process elements left over in  stack.
    r_index = len(h)
    while(stack):
      calculate_area(areas, stack, r_index)
    return max(areas)
      
if __name__ == "__main__":
    n = int(raw_input().strip())
    h = map(int, raw_input().strip().split(' '))
    result = largestRectangle(h)
    print result
