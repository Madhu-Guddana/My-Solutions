# Question: https://practice.geeksforgeeks.org/problems/closest-palindrome/0
# Algorithm: https://www.geeksforgeeks.org/given-a-number-find-next-smallest-palindrome-larger-than-this-number/

def is_palindrom(arr):
  # This is no where used, as it was not requried.
  i=0 
  j = len(arr)-1
  while (i<j):
    if arr[i]!= arr[j]:
      return False
    i = i+1
    j = j-1
  return True

def arr_to_num(arr):
  sum = 0
  for i, item in enumerate(reversed(arr)):
    sum = sum + item* (10**i)
  return sum

def num_to_arr(num):
  arr = []
  while num:
    arr.append(num%10)
    num=num//10
  return arr[::-1]

def append_mirror_image(arr, include_mid):
  # Generates the palindrome, by mirroring the existing arr.
  # length of result must be odd or even will be decided by include_mid variable
  i = len(arr)-1
  if not include_mid:
    i-=1
  while i>=0:
    arr.append(arr[i])
    i-=1
  return arr

def provide_half_array(arr):
  # Simply provide half of the element, in case of odd number this include mid element as well
  temp_len = len(arr)
  if temp_len%2 == 1:
    temp_len = temp_len+1
  mid = temp_len//2
  return arr[0:mid]

def get_lower_palindrome(pal_arr):
  # Provides a num, that is lesser than input and is palindrome.
  
  # Special Case.
  if pal_arr == [1,1]:
    return 9

  # Decrease number from mid.
  arr = provide_half_array(pal_arr)
  temp_len = len(arr)
  num = arr_to_num(arr)-1
  arr = num_to_arr(num)
  # Special case, where number of digits decreses. eg:10 has come to 9.
  if len(arr)!=temp_len:
    # Make sure you have reallocated the memory
    pal_arr = [9 for _ in range(len(pal_arr)-1)]
    return arr_to_num(pal_arr)

  # include mid element for mirroring, if given pal is even lenght
  include_mid = (len(pal_arr)%2==0)
  append_mirror_image(arr,include_mid)
  return arr_to_num(arr)

def get_higher_palindrome(pal_arr):
  # Provides a num, that is greater than input and is palindrome.
  
  # Increase number from mid.
  arr = provide_half_array(pal_arr)
  temp_len = len(arr)
  num = arr_to_num(arr)+1
  arr = num_to_arr(num)
  # Special case, where number of digits decreses. eg:9 has come to 10.
  if len(arr)!=temp_len:
    pal_arr = [0 for _ in range(len(pal_arr))]
    pal_arr[0]=1
    pal_arr.append(1)
    return arr_to_num(pal_arr)

  # include mid element for mirroring, if given pal is even lenght
  include_mid = (len(pal_arr)%2==0)
  append_mirror_image(arr,include_mid)
  return arr_to_num(arr)

def solve(num):
  # Actual entry point for the problem
  if num<10:
      return num-1
  arr = num_to_arr(num)
#   if is_palindrom(arr):
#     return num
    
  
  i = len(arr)//2
  if len(arr)%2 == 1:
    j = i+1
  else:
    j = i
  i = i-1

  smaller = None
  while(i>=0 and j<len(arr)):
    if arr[i] == arr[j]:
      i = i-1
      j = j+1
      continue

    if smaller == None:
      smaller = bool(arr[i] < arr[j])
    arr[j] = arr[i]


  if smaller == True:
    lower_palindrom = arr_to_num(arr)
    higher_palindrome = get_higher_palindrome(arr)
  elif smaller==False:
    lower_palindrom,  = get_lower_palindrome(arr),
    higher_palindrome = arr_to_num(arr)
  else:
    lower_palindrom  = get_lower_palindrome(arr)
    higher_palindrome = get_higher_palindrome(arr)

  return lower_palindrom if num-lower_palindrom <= higher_palindrome-num else higher_palindrome

for _ in range(int(input())):
  num = int(input())
  print(solve(num))


