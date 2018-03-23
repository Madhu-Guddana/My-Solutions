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

# DP gives, the cummulative profit gained, if we select a village. 
# key is face profit value of village, value is cummulative value
# Eg: [1,2,3,4,5,6] 
# if you visit 1, you can visit 1->2->4 or 1->3->6. so dp[1] = max(1+2+4, 1+3+6)
dp = {} # Dict, since search time is 0.

# Visting each village, will atlease give its face value as profit.
for profit in arr:
  dp[profit]=profit
max_num = arr[-1]

# Maximum face value of profit.
u_limit = 100000

# Going from max profit.
for item in reversed(arr):
  profits = [item]
  for i in range(2,u_limit): # check with all multiples of item.
    place = item * i
    if place > max_num:
      break
    # The reason to come from max element is that, dp will have info, 
    # each element traversed so far will tell what max profit a village can give, if he visit this village and go further.
    profit = item + dp.get(place,0) 
    profits.append(profit)
  dp[item] = max(profits) # Max value of all alternative available.

print dp
print max(dp.values())
