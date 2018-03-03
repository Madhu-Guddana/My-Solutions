# Question:
# https://www.hackerrank.com/challenges/minimum-average-waiting-time/problem
# Basically LRU of tasks, which arrives at different point of time


import heapq


class node(object):
  def __init__(self,start_time, making_time):
    self.start_time =start_time
    self.making_time = making_time

  def __cmp__(self, other):
    return self.making_time - other.making_time

  def __repr__(self):
    return "(%s, %s)" % (self.start_time, self.making_time)

def update_cur_pointer(arr, pool, cur_pointer, cur_time):
  while(cur_pointer< len(arr) and arr[cur_pointer].start_time<=cur_time):
    heapq.heappush(pool, arr[cur_pointer])
    cur_pointer+=1
  return cur_pointer

if __name__ == "__main__":
  N = int(raw_input())
  arr = []
  for _ in range(N):
    start_time, making_time = str(raw_input()).split(' ')
    arr.append(node(int(start_time), int(making_time)))

  arr.sort(key= lambda x:x.start_time)
  pool = []
  cur_time = arr[0].start_time
  cur_pointer = update_cur_pointer(arr, pool, 0, cur_time)

  wait_time_sum = 0
  while(cur_pointer<len(arr) or pool):
    try:
      job = heapq.heappop(pool)
    except IndexError:
      cur_time+=1
      cur_pointer = update_cur_pointer(arr, pool, cur_pointer, cur_time)
      continue
    cur_time+=job.making_time
    wait_time = cur_time-job.start_time
    wait_time_sum+=wait_time
    cur_pointer = update_cur_pointer(arr, pool, cur_pointer, cur_time)

  print wait_time_sum//len(arr)

