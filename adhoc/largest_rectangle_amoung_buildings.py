# This was very intersting problem.

# Question:
# Given a list of building heights in order from left to right, assuming the buildings are adjacent, 
# calculate the largest rectangle you could form choosing any segment of the line of buildings.

# Clue for O(n) solution:
# If we have l_index and r_index, which are less than cur_index we can easily calculate area covered by keeping this 
# rectangle as smallest in our answer.
# Find r_index (easy) While we traverse, if we get element less than cur element, then that is r_index.
# Find l_index (use stack). Maintain a stack whoes element are always in accending order.
# Once we calculate area for a index, we will populate a array area, and that will not be in stack at all.



# Sources:
# 1) https://www.hackerrank.com/challenges/largest-rectangle/problem
# 2) https://www.geeksforgeeks.org/largest-rectangle-under-histogram/


#!/bin/python

import sys

def calculate_area(areas,stack, r_index):
    
    # calculate area of top_ele and populate the same in area[].
    top_ele = stack.pop()
    t_index, t_item = top_ele[0], top_ele[1]
    l_index = stack[-1][0] if stack else -1
    
    # area doesn't include r_index and l_index, also index starts with 0.
    size = r_index-l_index-1
    area = t_item*(size)
    areas[t_index] = area

def largestRectangle(heights):
    stack = []
    if not heights:
      return 0
    
    # Initialize areas to 0
    areas = [0]*len(heights)
    
    # Stack structure [ (index, element)]
    stack.append((0,heights[0]))
    
    # First element is traversed, proceeding with other elements.
    for index in range(1,len(heights)):
      item = heights[index]
      while stack and item < stack[-1][1]: # If we found r_index for the top element.
        
        # This will calculate area of top element, pop it from stack and populate it in area[]
        # So every traversing, will keep reducing stack by 1 element.
        calculate_area(areas, stack, index) 
      
      # So now we deleted all elements, which are less than item. We can push item to stack.
      stack.append((index, item))
    
    # Process elements left over in  stack.
    r_index = len(heights)
    while(stack):
      calculate_area(areas, stack, r_index)
    return max(areas)
      
if __name__ == "__main__":
    n = int(raw_input().strip())
    h = map(int, raw_input().strip().split(' '))
    result = largestRectangle(h)
    print result
