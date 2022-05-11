###
# 19237. 어른 상어
# problem : https://solved.ac/search?query=19237
# status : solved
###

from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]

N,M,K = map(int,input().split())
smell = [[0]*N for _ in range(N)]
shark = []
for i in range(N):
  tmp = list(map(int,input().split()))
  for j in range(N):
    if tmp[j] > 0:
      shark.append((tmp[j],j,i))
      smell[i][j] = [tmp[j], K]
shark = deque(sorted(shark))
direction = [0]+list(map(int,input().split()))
priority = [0]+[[0]+[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]

for i in range(1, 1001):
  visited = [[False]*N for _ in range(N)]
  for _ in range(len(shark)):
    flg = False
    num, x, y = shark.popleft()
    dir = direction[num]
    for j in priority[num][dir]:
      ax, ay = x+dx[j], y+dy[j]
      if -1 < ax < N and -1 < ay < N :
        if smell[ay][ax] == 0 :
          flg = True
          break
    if not flg :
      for j in priority[num][dir]:
        ax, ay = x+dx[j], y+dy[j]
        if -1 < ax < N and -1 < ay < N :
          if smell[ay][ax][0] == num :
            break
    if visited[ay][ax] : continue
    direction[num] = j
    visited[ay][ax] = True
    shark.append((num,ax,ay))
  if len(shark) == 1 :
    print(i)
    exit()
  for num, x, y in shark:
    smell[y][x] = [num, K+1]
  for j in range(N):
    for k in range(N):
      if smell[j][k] != 0 :
        if smell[j][k][1] > 1 :
          smell[j][k][1] -= 1
        elif smell[j][k][1] == 1 :
          smell[j][k] = 0
print(-1)

