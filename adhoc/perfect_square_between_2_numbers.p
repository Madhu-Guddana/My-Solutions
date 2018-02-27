#!/bin/python

# Question:
# Watson gives two integers ( A andB  ) to Sherlock and asks if he can count the number
# of square integers between  A and B  (both inclusive):
#
# Sources: 
# 1) https://www.hackerrank.com/challenges/sherlock-and-squares/problem
# 2) https://practice.geeksforgeeks.org/company/Ola-Cabs/

import sys
import math

def squares(a, b):
    
    a_sqrt = int(math.sqrt(a))
    b_sqrt = int(math.sqrt(b))
    if a_sqrt == b_sqrt and a_sqrt*b_sqrt ==a:
      return 1
    return b_sqrt - a_sqrt

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        a, b = raw_input().strip().split(' ')
        a, b = [int(a), int(b)]
        result = squares(a, b)
        print result

