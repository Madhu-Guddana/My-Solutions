# Solution for questions.
# 1. https://practice.geeksforgeeks.org/problems/find-median-in-a-stream/0
# 2. https://www.hackerrank.com/challenges/find-the-running-median/problem

# Problem Statement:
# Given an input stream of n integers the task is to insert integers to 
# stream and print the median of the new stream formed by each insertion of x to the stream.

# The first line of input contains an integer N denoting the no of elements of the stream.
# Then the next N lines contains integer x denoting the no to be inserted to the stream.

# Solution:
# We maintain max heap on left side and min heap on right side.
# When a new element comes, if item <= left[0] then heappush to right, and rebalance both the trees.
# Any time you want median, if len(left) == len(right) then ans = (left[0]+right[0])/2.0 else
# ans = left[0] or right[0], based on tree length.
import heapq

N = int(raw_input())
left_max_heap = []
right_min_heap = []

def add_item(item):

  # python doesn't support max_heap, so we negate the element and save it.
  if not left_max_heap or item <= -1 * left_max_heap[0]:
    heapq.heappush(left_max_heap, -1 * item)
  else:
    heapq.heappush(right_min_heap, item)

def rebalance():
  len1 = len(left_max_heap)
  len2 = len(right_min_heap)
  if len1 == len2 or abs(len1-len2) == 1:
    return

  if len1 > len2:

    # python doesn't support max_heap, so we negate the element and save it.
    item = -1 * heapq.heappop(left_max_heap)
    heapq.heappush(right_min_heap, item)
  else:
    item = -1* heapq.heappop(right_min_heap)
    heapq.heappush(left_max_heap, item)

def get_median():
  len1 = len(left_max_heap)
  len2 = len(right_min_heap)
  if len1 == len2:
    return (-1* left_max_heap[0]+ right_min_heap[0])/2.0

  if len1 > len2:
    item = -1 * left_max_heap[0]
  else:
    item = right_min_heap[0]

  return float(item)

for _ in range(N):
  item = int(raw_input())
  add_item(item)
  rebalance()
  print get_median()
  print left_max_heap
  print right_min_heap
