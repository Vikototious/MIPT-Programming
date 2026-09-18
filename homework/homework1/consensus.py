'''
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
'''

def solve():
  n = 8
  profile_A = [0] * n
  profile_C = [0] * n
  profile_G = [0] * n
  profile_T = [0] * n
  
  for i in range(7):
    name = input()
    s = input()
    
    for i in range(len(s)):
      match s[i]:
        case 'A':
          profile_A[i] += 1
        case 'C':
          profile_C[i] += 1
        case 'G':
          profile_G[i] += 1
        case 'T':
          profile_T[i] += 1
  
  consensus = [''] * n
  
  for i in range(len(consensus)):
    counts = [profile_A[i], profile_C[i], profile_G[i], profile_T[i]]
    
    max_index = counts.index(max(counts))
    match max_index:
      case 0:
        consensus[i] = 'A'
      case 1:
        consensus[i] = 'C'
      case 2:
        consensus[i] = 'G'
      case 3:
        consensus[i] = 'T'
        
  
  for char in consensus:
    print(char, end='')
  print()
  print('A:', *profile_A)
  print('C:', *profile_C)
  print('G:', *profile_G)
  print('T:', *profile_T)
  
    
solve()

'''
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
'''
