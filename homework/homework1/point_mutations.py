'''
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
'''

def solve():
  a = input()
  b = input()
  
  d = 0
  
  for i in range(len(a)):
    if a[i] != b[i]:
      d += 1
      
  print(d)
  
solve()

#7