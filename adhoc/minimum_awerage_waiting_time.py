# Source:
# https://www.hackerrank.com/challenges/minimum-average-waiting-time/problem

# Question:
# Orders in pizza counter will come at different point of time and differnt type of pizza takes different amount of time.
# Process the order such that average waiting time of customer is less

# Solution:
# Non-premptive shortest job first is the solution.

import heapq


class node(object):
  def __init__(self,start_time, making_time):
    self.start_time =start_time
    self.making_time = making_time

  def __cmp__(self, other): # used for sorting.
    return self.making_time - other.making_time

  def __repr__(self):
    return "(%s, %s)" % (self.start_time, self.making_time)

def update_cur_pointer(arr, pool, cur_pointer, cur_time):
  # Add all the orders till cur_time to pool ( the heap).
  while(cur_pointer< len(arr) and arr[cur_pointer].start_time<=cur_time):
    heapq.heappush(pool, arr[cur_pointer])
    cur_pointer+=1
  
  # Return, the cur_pointer, which points to order that has not yet came in w.r.t cur_time.
  return cur_pointer

if __name__ == "__main__":
  N = int(raw_input())
  arr = []
  for _ in range(N):
    start_time, making_time = str(raw_input()).split(' ')
    arr.append(node(int(start_time), int(making_time)))

  # Sort array based on pizza preparation time.
  arr.sort(key= lambda x:x.start_time)
  pool = []
  cur_time = arr[0].start_time
  cur_pointer = update_cur_pointer(arr, pool, 0, cur_time)

  wait_time_sum = 0
  
  # While we have orders.
  while(cur_pointer<len(arr) or pool):
    try:
      job = heapq.heappop(pool)
    except IndexError:
      
      # No order to process at cur point of time. so increase the time.
      cur_time+=1
      cur_pointer = update_cur_pointer(arr, pool, cur_pointer, cur_time)
      continue
    cur_time+=job.making_time
    wait_time = cur_time-job.start_time
    wait_time_sum+=wait_time
    cur_pointer = update_cur_pointer(arr, pool, cur_pointer, cur_time)

  print wait_time_sum//len(arr)
