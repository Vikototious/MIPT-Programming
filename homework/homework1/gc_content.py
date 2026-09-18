'''
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT
'''
def solve():
  def gc_count(s):

    cnt = 0

    for character in s:
      if character == 'C' or character == 'G':
        cnt += 1

    return cnt / len(s)


  ans_name = ''
  ans_count = -1

  t = 3

  for i in range(t):
    
    name = input()

    string = input()
    res = gc_count(string)
    
    if res > ans_count:
      ans_count = res
      ans_name = name
      
  print(ans_name)
  print(ans_count * 100)
  
solve()
#>Rosalind_0808
#60.91954022988506