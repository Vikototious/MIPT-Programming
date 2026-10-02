'''
def fib(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fib(n - 1) + fib(n - 1)

print(fib(10))
'''

n = int(input)

A = [0 for _ in range(n + 1)]
def fib_memo(n, fibs):
  if n == 0:
    fibs[n] = 0
    return 0
  if n == 1:
    fibs[n] = 1
    return 1
  if fibs[n] == 0:
    return fibs[n - 1]
  fibs[n - 1] = fib_memo(n - 1, fibs) + fib_memo(n - 2, fibs)
  return fibs[n - 1]

print(fib_memo(n , A))

'''
def fib_dyn(n):
  dp = [0 for i in range(n)]
  dp[0] = 0
  dp[1] = 1
  for i in range(2, n):
    dp[i] = dp[i - 1] + dp[i - 2]
  print(dp)
  return dp[i]

print(fib_dyn(10))
'''
def levenstein(s1, s2):
  l1 = len(s1)
  l2 = len(s2)
  dp = [[0 for _ in range(l2)] for _ in range(l1)]
  for i in range(l1):
    dp[i][0] = i
  for j in range(l2):
    dp[0][j] = j
  
  for i in range(l1):
    for j in range(l2):
      flag = s1[i] != s2[j]
      dp[i][j] = min(
        dp[i - 1][j] + 1,
        dp[i][j - 1] + 1,
        dp[i - 1][j - 1] + flag
      )
  return dp[-1][-1]
  
print(levenstein('abca', 'abd'))
