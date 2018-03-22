# Question :
# Two Suppliers A and B can attend X and Y number of customers.
# There are total N customers where N <= X+Y.
# Each customer will give different value of tips of A and B (either for A or B, not both).
# Find Maximum sum of tips possible.
#
# Source:
# https://practice.geeksforgeeks.org/problems/maximum-tip-calculator/0

T = int(input())
for _ in range(T):
  N, X, Y = input().split(' ')
  N, X, Y = int(N), int(X), int(Y)
  A = [int(i) for i in input().split(' ') if i.isdigit()]
  B = [int(i) for i in input().split(' ') if i.isdigit()]
  
  # This is to handel wrong inputs, you can ignore this.
  if N > len(A) or N> len(B):
    N = min(len(A), len(B))
  if N < len(A) or N < len(B):
    A=A[:N]
    B=B[:N]


  tips = list(zip(A,B))

  # Sort tips, such that, right side elements are those which gives more tips to A compare to B.
  # Left side elements are those which are in favour or B.
  tips.sort(key=lambda money: money[0]-money[1])
  
  a = N -1 # index for A
  b = 0 # index for B

  # minimum of how much A can Handle, B can Handle or half of the list.
  # Till this, we can care freely select elements
  minimum = min(X,Y,N//2)
  
  count = 0
  while(a>=b): # Traverse all elements.
      # If b is exhauted, or if 'a' gives better profit than b. then select a.
      if b==Y or  (a<X and tips[a][0]-tips[a][1] > tips[b][1]-tips[b][0]):
        count +=tips[a][0]
        b+=1
      else:
        count += tips[b][1]
        a-=1
  print (count)

