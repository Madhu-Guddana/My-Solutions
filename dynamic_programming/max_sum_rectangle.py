# Question:
# Given a 2D array, find the maximum sum subarray in it
# Source:
# 1) https://practice.geeksforgeeks.org/problems/maximum-sum-rectangle/0
# 2) https://www.youtube.com/watch?v=yCQN096CwWM
# 3) https://www.hackerrank.com/contests/pscg-coding-contest-march-2016/challenges/maximum-sub-matrix

def kadane(arr):
  low = temp_low = high = temp_max = 0
  max_sofar = arr[0] if arr else 0
  for i in range(len(arr)):
    temp_max = temp_max+arr[i]

    if max_sofar < temp_max:
      max_sofar = temp_max
      high = i
      low = temp_low


    if temp_max < 0:
      temp_max=0
      temp_low = i+1
  return (max_sofar, low, high)

def max_rect_sum(arr):
  if not arr or not arr[0]:
    return 0
  max_sum = arr[0][0]
  l = r = t = d = 0 # left right top down
  for i in range(len(arr)): # Consider each row, check if max_array start from here.
    # temp_arr used for incremental sum.
    temp_arr = [0]*len(arr[0])
    
    for j in range(i, len(arr)): # Find max_arr possible with row starting i and ending with j.

      # Array under consideration is arr[i:j+1]
      # Add the correcponding element of jth row elements to temp_arr.
      # Since incremental sum, this will be equal to adding each elements of a col in arr[i:j+1]
      temp_arr = [temp_arr[k]+ arr[j][k] for k in range(len(arr[j]))] # Convert 2D to 1D matrix by sum.

      temp_sum, left, right = kadane(temp_arr)
      if temp_sum > max_sum:
        l,r,t,d = left, right, i, j
        max_sum = temp_sum

  return max_sum

arr = [
  [1,  2, -1,-4,-20],
  [-8,-3,  4, 2,  1],
  [3,  8, 10, 1,  3],
  [-4,-1,  1, 7, -6]
]
print (max_rect_sum(arr))
# Expected Answer: 29
