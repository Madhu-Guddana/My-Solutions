# Good Number: A number is said to be good, if digits are in non decreasing order from left to right.

# Question:
# Given a number, return a biggest good number that is <= given number.


# Algorithm
# Traverse digits from left to right.
# When ever you see a digit, that doesn't follow the rule, do following
# Digit just before this must be decreased by 1.
# Digits from the cur position must be made as 9.
# Example 1207, here 0 voilates the rule, so transaction is 1207 --> 1107 -->1199.

# Corner cases
# 1. The number to decrease by one, is not just index-1, it could be before that as well.
#    Example: 1221 -> 1211 is wrong
#             1221 -> 1121 -> 1111 - > 1119.
#    So all the number to the left, that are equal to 2, will be decrement by 1.
# 2. In the above approach, it is possible that all digits from left side must be decresed by 1.
#    In this case, after decreasing, all digits except MSB must be made 9.
#    Example: 2220 -> 1119 -> 1999
#             1110 -> 0009 -> 0999


def get_currupt_index(arr):
  """
  Returns the index of the number which voilated the rule.
  eg:- 1110 returns 3.
       121 returns 2.
  """
  for index in range(1,len(arr)):
    if arr[index]<arr[index-1]:
      return index
  return len(arr)

def num_to_arr(num):
  """
  Converts number to Array
  """
  arr = []
  if num==0:
    return [0]

  while num:
    rem = num%10
    arr.append(rem)
    num = num/10
  return arr[::-1]

def arr_to_num(arr):
  ans = 0
  for num in arr:
    ans = ans*10+num
  return ans

def set_lsb_to_nine(arr, index):
  """
  From index to last, make all digit as 9.
  """
  for i in range(index, len(arr)):
    arr[i]=9


def decrease_msb(old_num, arr, index):
  """
  This has many cases to consider.
  1. decrese all the number that is equal to old_num. This covers the corner case 1 explained.
  2. If the number of decreased digits is equal to all the left digits from index, then we need to fill all left number 
  with 9 except the MSB. This will cover the 2nd corner case.
  """
  count = 0
  for i in range(0, index):
    if arr[i] == old_num:
      count +=1
      arr[i] = old_num-1
  if count == index :
    for i in range(1, index):
      arr[i] = 9

def solve(num):
  arr = num_to_arr(num)
  index = get_currupt_index(arr)
  if index == len(arr):
    return num

  old_num = arr[index-1]

  decrease_msb(old_num, arr, index)
  set_lsb_to_nine(arr,index)
  return arr_to_num(arr)


print solve(2220)
