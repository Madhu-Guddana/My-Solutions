# Find number of 1 in binary representation of a number.
def set_bit(num):
  ans = 0
  while num:
    num = num&num-1
    ans = ans+1
  return ans

for i in range(16):
  print set_bit(i)
