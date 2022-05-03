###
# 16234. 인구 이동
# problem : https://www.acmicpc.net/problem/16234
# status : solved (pypy3)
###

import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N,L,R = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]

cnt = 0
while True :
  visited = [[False]*N for _ in range(N)]
  flg = False
  for i in range(N):
    for j in range(N):
      if not visited[i][j] :
        visited[i][j] = True
        q = deque([(j,i)])
        tmp_lst = [(j,i)]
        S, C = lst[i][j], 1
        while q :
          x, y = q.popleft()
          for k in range(4):
            ax, ay = x+dx[k], y+dy[k]
            if -1<ax<N and -1<ay<N and not visited[ay][ax] and L<=abs(lst[ay][ax]-lst[y][x])<=R:
              visited[ay][ax] = True
              tmp_lst.append((ax,ay))
              q.append((ax,ay))
              S += lst[ay][ax]
              C += 1
        if C > 1 :
          flg = True
          n = S // C
          for x, y in tmp_lst :
            lst[y][x] = n
  if not flg : break
  cnt += 1
print(cnt)
