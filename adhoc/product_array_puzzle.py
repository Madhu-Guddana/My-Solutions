# Though this looks simple, one must have to take care of multiple corner cases

# Question:
# Given an array arr[] of n integers,
# construct a Product Array prod[] (of same size) such that prod[i] 
# is equal to the product of all the elements of arr[] except arr[i].

# Corner Cases:
# 1. No Element in arr
# 2. Only one element in array
# 3. One 0 present in arr
# 4. More than one 0 present in arr.

# Source:
# https://practice.geeksforgeeks.org/problems/product-array-puzzle/0

from functools import reduce

T = int(input())
for _ in range(T):
    N = int(input())
    zero_index = []
    arr = []
    for index, ele in enumerate(input().split(' ')):
        if not ele.isdigit():
            continue
        arr.append(int(ele))
        
        if ele == 0:
            zero_index.append(index)

    if len(arr) == 1:
        print (0)
    elif len(zero_index) > 1:
        for _ in range(N):
            print (0, end=' ')
    else:
        product = 1
        for ele in arr:
            if ele: product *= ele
        
        if len(zero_index) == 1:
            for index in range(len(arr)):
                if index == zero_index[0]:
                    print (product, end = ' ')
                else:
                    print (0, end = ' ')
        else:
            for ele in arr:
                print (product//ele, end = ' ')
    print ()
                
