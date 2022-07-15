###
# 16918. 봄버맨
# problem : https://www.acmicpc.net/problem/16918
# status : solved
# time : 00:28:39
###

R, C, N = map(int, input().split())
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
if N == 1 :
  for _ in range(R):
    print(input().strip())
  exit()
  
map_lst = []
for i in range(R):
  map_lst.append([-1 if x == '.' else 1 for x in input().strip()])

t = 1
while True :
  for i in range(R):
    for j in range(C):
      if map_lst[i][j] > 0 :
        map_lst[i][j] -= 1
      else :
        map_lst[i][j] = 2
  t += 1
  if t == N : break

  tmp = set()
  for i in range(R):
    for j in range(C):
      if map_lst[i][j] == 0 :
        for k in range(5):
          tmp.add((j+dx[k],i+dy[k]))
      else :
        map_lst[i][j] -= 1
        
  for x, y in tmp :
    if not (-1<x<C and -1<y<R) : continue
    map_lst[y][x] = -1
  t += 1
  if t == N : break

for m in map_lst:
  print(''.join(['.' if x == -1 else 'O' for x in m]))
