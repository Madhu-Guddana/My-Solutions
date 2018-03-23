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
    temp_arr = [0]*len(arr[0])
    for j in range(i, len(arr)): # Find max_arr possible with i as starting index.
      temp_arr = [temp_arr[k]+ arr[j][k] for k in range(len(arr[j]))]
      temp_sum, left, right = kadane(temp_arr)
      if temp_sum > max_sum:
        l,r,t,d = left, right, i, j
        max_sum = temp_sum

  return max_sum


for _ in range(int(input())):
  n, m = input().split(' ')
  n, m = int(n), int(m)
  temp_arr = input().split(' ')
  arr = []
  for i in range(n):
    a = []
    for j in range(m):
      a.append(int(temp_arr[i*m+j]))
    arr.append(a)
  print (max_rect_sum(arr))
