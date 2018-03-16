# Given an unsorted array say [11,2,3,9,5,6,8], which indicate profit that can be gained in various village.
# Each time you visit a village, you will add that profit into your account
# Conditions here are
# 1. You should always allowed only to go to village from lower profit to higher profit. eg: 8 -> 2 is not allowed, 2->8 is allowed
# 2. You should always allowed only to go to village, whose profit is multiple of present village profit. eg: 3 -> 6 is allowed, 6->9 
# is not allowed.

# Constraints:
# 1<=profit<100000
# 1<=number_of_village<100000

arr = [11,2,3,9,5,6,8]
arr.sort()
dp = {}
for profit in arr:
  dp[profit]=profit
max_num = arr[-1]
u_limit = 100000

for item in reversed(arr):
  profits = [item]
  for i in range(2,u_limit):
    place = item * i
    if place > max_num:
      break
    profit = item + dp.get(place,0)
    profits.append(profit)
  dp[item] = max(profits)

print dp
print max(dp.values())
