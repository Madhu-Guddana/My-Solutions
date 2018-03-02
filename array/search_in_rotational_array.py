# Question:
# Given a sorted and rotated array (rotated at some point) A[ ], 
# and given an element K, the task is to find the index of the given 
# element K in the array A[ ]. The array has no duplicate elements. 
# If the element does not exist in the array, print -1.

# Source:
# https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array/0

def element_in_left(arr, low, mid, high, item):
"""Basic theory here is, array is in sorted order either left side or right side.
If array is in sorted order, we can check range and say if item falls under the range.
"""
  if arr[low] < arr[mid]: # Left side array is sorted
    if arr[low]<= item < arr[mid]:
      return True
    else:
      return False
  else: # Right side array is sorted
    if arr[mid] < item <= arr[high]:
      return False
    else:
      return True

def binary_search(arr, item):
  low = 0
  high=len(arr)-1

  while(low<=high):
    mid = (low+high)//2
    if item == arr[mid]:
      return mid
    if element_in_left(arr, low, mid, high, item):
      high = mid-1
    else:
      low = mid+1
  return -1

T = int(input())
for _ in range(T):
  N = int(input())
  arr = str(input()).split(' ')
  item = int(input())
  arr = [int(ele) for ele in arr if ele.isdigit()]
  print (binary_search(arr, item))
