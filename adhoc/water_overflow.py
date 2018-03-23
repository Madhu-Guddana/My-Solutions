# Question:
# There is a stack of water glasses in a form of pascal triangle and a person
# wants to pour the water at the topmost glass, but the capacity of each glass
# is 1 unit . Overflow takes place in such a way that after 1 unit, 1/2 of remaining
# unit gets into bottom left glass and other half in bottom right glass.
#
# Now the pours K units of water in the topmost glass and wants to know how
# much water is there in the jth glass of the ith row.
#
# Assume that there are enough glasses in the triangle till no glass overflows.

# Source:
# https://www.geeksforgeeks.org/find-water-in-a-glass/

# Explanation:
# Source: http://www.ritambhara.in/water-overflowing-from-glass-arranged-in-form-of-triangle/
# Consider row starts with number 1,
# At each row i there will i number of glasses, so 2 dimension matrix can be used to represent this structure easily.
# Solution is via recursive.
# I put all the K liter in First glass(i=0, j=0), the excess water it will give to (i=1,j=0 and i=1,j=1)
# We can use recursive code, and base condition is where K becomes 0.

def fill_water(G, i, j, K):
  if K==0:
    return
  # 1 is the capacity of the glass, G[i][j] might have some amount of water, filled in the recursive process during some other iteration.
  capacity = 1-G[i][j] 
  available_water = capacity if capacity<K else K # Available water may not be upto capacity, so this condition.
  G[i][j] += available_water
  K -= available_water
  fill_water(G,i+1,j,K/2.0)
  fill_water(G,i+1,j+1,K/2.0)
 
for _ in range(int(input())):
  K = int(input())
  G = [[0]*j for j in range (1,K)]
  fill_water(G, 0, 0, K)
  i = int(input())
  j = int(input())
  print (G[i-1][j-1])
