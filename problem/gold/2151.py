###
# 2151. 거울 설치
# problem : https://www.acmicpc.net/problem/2151
# status : solved
###

from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

INF = float('inf')
ans = INF
N = int(input())
d = []
lst = [input().strip() for _ in range(N)]
for i in range(N):
  for j in range(N):
    if lst[i][j] == '#':
      d.append((j,i))

(sx, sy), (tx, ty) = d[0], d[1]
q = deque([])
visited = [[[INF]*N for _ in range(N)] for _ in range(4)]
for i in range(4) :
  q.append((sx,sy,0,i))
  visited[i][sy][sx] = True
  
while q :
  x, y, c, d = q.popleft()
  
  ax, ay = x+dx[d], y+dy[d]
  if (ax, ay) == (tx, ty) :
    ans = min(ans, c)
    continue
  if -1 < ax < N and -1 < ay < N and c < visited[d][ay][ax]:
    if lst[ay][ax] == '!':
      for i in [-1, 0, 1]:
        ad = (d + i) % 4
        visited[ad][ay][ax] = c+abs(i)
        q.append((ax,ay,c+abs(i),ad))
    elif lst[ay][ax] == '.':
      visited[d][ay][ax] = c
      q.append((ax,ay,c,d))

print(ans)
