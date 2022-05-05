###
# 17142. 연구소 3
# problem : https://www.acmicpc.net/problem/17142
# status : solved
###

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
v_lst = []
ans = 50*50+1
cnt0 = 0
for i in range(N):
  for j in range(N):
    if lst[i][j] == 2 :
      v_lst.append((j,i))
    elif lst[i][j] == 0 :
      cnt0 += 1
v_visit = [False]*len(v_lst)

def solve(c, now, v):
  global ans
  if c < M:
    if now >= len(v_lst) : return
    for i in range(now, len(v_lst)):
      solve(c+1, i+1, v+[v_lst[i]])
    return
  
  q = deque([])
  visited = [[False]*N for _ in range(N)]
  for x, y in v :
    q.append((x,y,0))
    visited[y][x] = True
  tmp = 0
  empty = 0
  while q :
    x, y, cnt = q.popleft()
    tmp = max(tmp, cnt)
    for i in range(4):
      ax, ay = x+dx[i], y+dy[i]
      if -1<ax<N and -1<ay<N and not visited[ay][ax] and lst[ay][ax] != 1 :
        visited[ay][ax] = True
        if lst[ay][ax] == 0 : empty += 1
        q.append((ax,ay,cnt+1))
    if empty == cnt0 : 
      ans = min(ans, cnt+1)
      break

if cnt0 != 0:
  solve(0, 0, [])
  print(ans if ans < 50*50+1 else -1)
else :
  print(0)
