# Question:
# Given a square chessboard of N x N size, the position of Knight and position of a target is given.
# We need to find out minimum steps a Knight will take to reach the target position.

Source: https://practice.geeksforgeeks.org/problems/steps-by-knight/0

def is_valid(mat, ele):
  N = len(mat)-1
  i = ele[0]
  j = ele[1]
  if not(0<=i<=N and 0<=j<=N):
    return False
  return (mat[i][j] == 0)

def get_neighbours(mat, subject):
  i = subject[0]
  j = subject[1]
  neigh = [(i-2, j-1),
           (i-2, j+1),
           (i-1, j-2),
           (i-1, j+2),
           (i+1, j-2),
           (i+1, j+2),
           (i+2, j-1),
           (i+2, j+1)]
  neigh = [ele for ele in  neigh if is_valid(mat, ele)]
  return neigh

def print_mat(mat):
  for row in mat:
    print row
  print "-"*80

def fill_matrix(mat, source):
  mat[source[0]][source[1]] = '*'
  queue = [source]
  queue.append('*')
  count = 0
  while queue:
    subject = queue.pop(0)
    if subject == '*':
      count+=1
      queue.append('*')
      if len(set(queue)) == 1:
        break
      continue
    neigh = get_neighbours(mat, subject)
    for ele in neigh:
      mat[ele[0]][ele[1]] = count+1
      queue.append(ele)

for T in range(int(raw_input())):
  N = int(raw_input())
  row = [0]*N
  mat = []
  for i in range(N):
    mat.append(row[:])

  source = str(raw_input()).split(' ')
  # source.strip()
  source = (int(source[0])-1, int(source[1])-1)
  
  target = str(raw_input()).split(' ')
  # target.strip()
  target = (int(target[0])-1, int(target[1])-1)

  fill_matrix(mat, source)
  mat[source[0]][source[1]] = 0
  
  print (mat[target[0]][target[1]])
