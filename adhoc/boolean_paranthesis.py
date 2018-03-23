# Given string of length n and n-1 which represents the bool str and operation resp.
# Eg:- str = TTFT and ops= '|&^', the final input will be T|T&F^T.

# Question: Find the number of ways, you can bracket the expression, so that it will results to True
# Examples:
# T | ((T & F) ^ T)  --> True
# T | (T & (F ^ T))  --> True
# (T | T) & F) ^ T   --> True
# (T | T) & (F ^ T)  --> True
# (T | (T & F)) ^ T  --> False
# Total ways = 5, Total ways for True = 4 and False = 1

# Algorithm.
# Consider A and B, where A and B are expression itself.
# Number of ways you can bracket A and B is as follows.
# we use notation F(A), T(A) and total(A).
#
#          | if op=='&' then T(A)*T(B)
# T(A,B) = | if op=='|' then total(A)*total(B)-F(A)*F(B)
#          | if op=='^' then T(A)*F(B) + F(A)*T(B)
#
#          | if op=='&' then total(A)*total(B) - T(A)*T(B)
# F(A,B) = | if op=='|' then F(A) * F(B)
#          | if op=='^' then F(A)F(B) + T(A)T(B)

# So we use Dynamic Programming.
# we divide expression to char by char and check for number of ways possible.
# We sum up all those ways.


def solve(str, ops):
  length = len(str)
  T = [[0]*length for _ in range(length)]
  F = [[0]*length for _ in range(length)]
  # In Both above matrix, only items above diagonal elements are touched,
  # below elements are never touched.

  # With single char, we can put paranthesis in either 1 way or
  # 0, based on its boolean value. So this stands as base condition
  for i in range(length):
    T[i][i] = 1 if str[i]=='T' else 0
    F[i][i] = 1 if str[i]=='F' else 0

  for window in range(1,length): # all possible size of window.
    for j in range(window,length): # Slide the window, j shows end of the window.
      i = j-window # i points to start of the window.
      for k in range(i,j): # Traverse inside window.
        char = ops[k]

        tik = T[i][k] + F[i][k]
        tkj = T[k+1][j] + F[k+1][j]

        if char == '&':
          T[i][j] += T[i][k]*T[k+1][j]
          F[i][j] += tik*tkj - T[i][k]*T[k+1][j]

        if char == '|':
          T[i][j] += tik*tkj - F[i][k]*F[k+1][j]
          F[i][j] += F[i][k]*F[k+1][j]

        if char == '^':
          T[i][j] += T[i][k]*F[k+1][j] + F[i][k]*T[k+1][j]
          F[i][j] += F[i][k]*F[k+1][j] + T[i][k]*T[k+1][j]

  # Note, answer risides in last element of 1st coloumn.
  return T[0][-1]
# T|T&F^T
print solve('TTFT', '|&^')

