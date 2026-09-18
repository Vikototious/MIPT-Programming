n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

state = list()

for i in range(4):
  line = list()
  for j in range(4):
    line.append(n[i + j * 4])
  state.append(line)
  
for line in state:
  print(line)
print()

sbox_s = [
[10, 14, 13, 5, 9, 7, 0, 6, 15, 4, 11, 8, 2, 12, 1, 3],
[0, 2, 11, 6, 8, 10, 5, 13, 15, 9, 12, 7, 1, 3, 14, 4],
[9, 3, 13, 5, 7, 11, 8, 6, 2, 4, 14, 15, 12, 0, 1, 10],
[7, 8, 5, 15, 11, 3, 9, 6, 2, 12, 1, 4, 14, 0, 10, 13],
[13, 12, 5, 15, 4, 0, 10, 9, 7, 8, 3, 2, 11, 6, 1, 14]
]

round1 = [[0] * 4 for i in range(4)]

for i in range(4):
  for j in range(4):
    round1[i][j] = sbox_s[0][state[i][j]]

for line in round1:
  print(line)
print()

for i in range(4):
  round1[i] = round1[i][i:] + round1[i][:i]
  
for line in round1:
  print(line)
print()

result = [[0] * 4 for _ in range(4)]

for c in range(4):
  s0 = round1[0][c]
  s1 = round1[1][c]
  s2 = round1[2][c]
  s3 = round1[3][c]
  
  result[0][c] = (s0 << 1) ^ ((s1 << 1) ^ s1) ^ s2 ^ s3
  result[1][c] = s0 ^ (s1 << 1) ^ ((s2 << 1) ^ s2) ^ s3
  result[2][c] = s0 ^ s1 ^ (s2 << 1) ^ ((s3 << 1) ^ s3)
  result[3][c] = ((s0 << 1) ^ s0) ^ s1 ^ s2 ^ (s3 << 1)
  
for line in result:
  print(line)
print()

for i in range(4):
  for j in range(4):
    result[i][j] = result[i][j] ^ sbox_s[0][i * 4 + j]
    
for line in result:
  print(line)
print()
