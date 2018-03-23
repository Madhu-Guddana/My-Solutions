# Given an array, find the part of array (consequitive elements) which results in max sum.

def kadane(arr):
  max_so_far = arr[0] if arr else 0
  temp_max = 0
  for ele in arr:
    temp_max += ele
    temp_max = max(0, max_ending)
    max_so_far = max(temp_max, max_so_far) # in case of all -ve number, 0 is the ans.
  return max_so_far
