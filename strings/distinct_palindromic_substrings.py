"""
Author: Madhu.Guddana

Solution for Problem: https://practice.geeksforgeeks.org/problems/distinct-palindromic-substrings/0
Time Complexity: O(n^2)
Using Dynamic Programing combined with recursion
"""

def is_paligdrome(string, i, j, PAL):
  if PAL[i][j]==-1:
    PAL[i][j]=int(string[i]==string[j] and is_paligdrome(string, i+1, j-1, PAL))
  return PAL[i][j]

T = int(raw_input())
for _ in range(T):
    string = str(raw_input())
    pal_collection = set()
    PAL = []
    for i in range(len(string)):
      PAL.append([-1]*len(string))
      PAL[i][i] = 1
      if i >0 and string[i] == string[i-1]:
        PAL[i][i-1] = 1
    for i in range(len(string)):
      for j in range(i, len(string)):
        if is_paligdrome(string,i, j, PAL):
          pal_collection.add(string[i:j+1])
    print (len(pal_collection))
