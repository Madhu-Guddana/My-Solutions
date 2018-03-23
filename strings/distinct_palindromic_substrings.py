"""
Author: Madhu.Guddana

Solution for Problem: https://practice.geeksforgeeks.org/problems/distinct-palindromic-substrings/0
Time Complexity: O(n^2)
Using Dynamic Programing combined with recursion

Eg:- dist_pal(abaaa) = ['a','b','aa', 'aba', 'aaa']

Algorithm:-
a string is processed by each 2 chars in each traverse.
In each traverse, string becomes palindrome, if it was palindrome without these chars and these 2 chars are equal.
"""

def is_paligdrome(string, i, j, PAL):
  if PAL[i][j]==-1:
    PAL[i][j]=int(string[i]==string[j] and is_paligdrome(string, i+1, j-1, PAL))
  return PAL[i][j]

T = int(raw_input())
for _ in range(T):
    string = str(raw_input())
    pal_collection = set() # To eleminate duplicates.
    PAL = []
    for i in range(len(string)): # Mark all as unvisted.
      PAL.append([-1]*len(string))
      
      # All single letter are palindrome
      PAL[i][i] = 1
      
      # Check for 2 letter plaindrome, this is the base condition for even length palindrome.
      if i >0 and string[i] == string[i-1]:
        PAL[i][i-1] = 1

    # Process all substring and check if it is a palindrome.
    for i in range(len(string)):
      for j in range(i, len(string)):
        if is_paligdrome(string,i, j, PAL):
          pal_collection.add(string[i:j+1])
    print (len(pal_collection))
