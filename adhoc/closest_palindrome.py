# Question: https://practice.geeksforgeeks.org/problems/closest-palindrome/0
# Given a number, find next near by palindrome.
# Eg: given 98 provide 99
# Given 90, provide 88.
# If number itself is a palindrome, give its neighbour palindrome
# If 101 give back 99
# If there are 2 closes palindrome, then give lower number amoung them
# If 10 is given, both 9 and 11 are nearby palindrome, then give 9 as answer.
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
  # Generates the palindrome, by mirroring and appending the existing arr.
  # length of result must be odd or even will be decided by include_mid variable
  # Eg: given [1,2,3] we return [1,2,3,3,2,1] if include_mid is true, else we return [1,2,3,2,1]
  i = len(arr)-1
  if not include_mid:
    i-=1
  while i>=0:
    arr.append(arr[i])
    i-=1
  return arr

def provide_half_array(arr):
  # Simply provide half of the element, in case of odd number this include mid element as well
  # Eg: [1,2,3,4] will return [1,2]
  # [1,2,3,4,5] will return [1,2,3]
  temp_len = len(arr)
  if temp_len%2 == 1:
    temp_len = temp_len+1
  mid = temp_len//2
  return arr[0:mid]

def get_lower_palindrome(pal_arr):
  # Provides a num, that is lesser than input and is palindrome.
  # Idea is- Decrease the mid element by 1, that must be enough.
  # But if mid element is 0, we need to propogate the substraction to its right, like how we do in normal substraction.
  # So the best way is:
  # 1) Bisect the array
  # 2) Convert it to num
  # 3) Substract it by 1
  # 4) Convert back to num
  # 5) Mirror the answer to make it reflective to the right part of the palindrome.
  
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
  # This is similar to get_lower_palindrome.
  # In fact we can avoid these code redundancy in production code.
  # For Practice and competition, this much is enough.
  
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
  
  # In case, we consider only nearest palindrome, we must uncomment following lines.
  #   if is_palindrom(arr):
  #     return num
    
  
  # i and j will point to characters that are mirror image(or altleast suppose to be mirror image).
  i = len(arr)//2
  if len(arr)%2 == 1:
    j = i+1
  else:
    j = i
  i = i-1

  # smaller indicates, if palindrome we got, is less than the num or not.
  smaller = None
  while(i>=0 and j<len(arr)):
    if arr[i] == arr[j]:
      i = i-1
      j = j+1
      continue
    arr[j] = arr[i]
    
    # Update smaller, only 1 time.
    if smaller == None:
      smaller = bool(arr[i] < arr[j])
 
  if smaller == True:
    lower_palindrom = arr_to_num(arr)
    higher_palindrome = get_higher_palindrome(arr)
  elif smaller==False:
    lower_palindrom,  = get_lower_palindrome(arr),
    higher_palindrome = arr_to_num(arr)
  else: # Case where number itself is palindrome.
    lower_palindrom  = get_lower_palindrome(arr)
    higher_palindrome = get_higher_palindrome(arr)

  return lower_palindrom if num-lower_palindrom <= higher_palindrome-num else higher_palindrome


#### Entry point for the programme ####
for _ in range(int(input())):
  num = int(input())
  print(solve(num))


