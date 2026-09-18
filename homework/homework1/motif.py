'''
GATATATGCATATACTT
ATAT
'''

def solve():
  string = input()
  substring = input()
  
  for i in range(len(string) - len(substring)):
    if string[i: i + len(substring)] == substring:
      print(i + 1, end=' ')
  
  
solve()
#2 4 10 