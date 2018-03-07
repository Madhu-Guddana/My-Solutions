# Question Source:
# https://practice.geeksforgeeks.org/problems/maximum-tip-calculator/0

T = int(input())
for _ in range(T):
  N, X, Y = input().split(' ')
  N, X, Y = int(N), int(X), int(Y)
  A = [int(i) for i in input().split(' ') if i.isdigit()]
  B = [int(i) for i in input().split(' ') if i.isdigit()]
  
  # This is to handel wrong inputs
  if N > len(A) or N> len(B):
    N = min(len(A), len(B))

  if N < len(A) or N < len(B):
    A=A[:N]
    B=B[:N]


  tips = list(zip(A,B))
  tips.sort(key=lambda a: a[0]-a[1])
  
  a = N -1
  b = 0
  minimum = min(X,Y,N//2)
  
  count = 0
  while(a>=b):
      if N-1-a>=X or (b<Y and tips[b][1]-tips[b][0] > tips[a][0]-tips[a][1]):
        count +=tips[b][1]
        b+=1
      else:
        count += tips[a][0]
        a-=1
  print (count)
