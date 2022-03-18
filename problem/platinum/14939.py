###
# 14939. 불 끄기
# problem : https://www.acmicpc.net/problem/14939
# status : solved
###
dx = [-1, 1, 0, 0, 0]
dy = [0, 0, 0, -1, 1]

lst = [input().strip() for _ in range(10)]
mp = [[False]*10 for _ in range(10)]

for i in range(10):
  for j in range(10):
    if lst[i][j] == 'O' : mp[i][j] = True

ans = 101
for i in range(1<<10):
  cnt = 0
  tmp = [lst[:] for lst in mp]
  for j in range(10):
    if i & (1<<j) :
      cnt += 1
      for k in range(5):
        x, y = j + dx[k], dy[k]
        if -1<x<10 and -1<y<10: tmp[y][x] = not tmp[y][x]
  
  for j in range(1,10):
    for k in range(10):
      if tmp[j-1][k] :
        cnt += 1
        for l in range(5):
          x, y = k + dx[l], j + dy[l]
          if -1<x<10 and -1<y<10: tmp[y][x] = not tmp[y][x]
  
  if sum(tmp[-1]) > 0 : continue
  ans = min(ans, cnt)
print(ans if ans < 101 else -1)
