###
# 16946. 벽 부수고 이동하기
# problem : https://www.acmicpc.net/problem/16946
# status : solved
###
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
lst = [[0]*m for _ in range(n)]
mp = [list(input().strip()) for _ in range(n)]
v = [[False]*m for _ in range(n)]

for i in range(n):
  for j in range(m):
    if mp[i][j] == '1':
      lst[i][j] += 1
      continue
    elif v[i][j] : continue
    v[i][j] = True
    q = deque([(j,i)])
    g = deque([])
    cnt = 1
    
    while q:
      x, y = q.pop()
      for k in range(4):
        ax = x + dx[k]
        ay = y + dy[k]
        if -1<ax<m and -1<ay<n and not v[ay][ax]:
          v[ay][ax] = True
          if mp[ay][ax] == '0' :
            cnt += 1
            q.append((ax,ay))
          else :
            g.append((ax,ay))

    for ax, ay in g:
      v[ay][ax] = False
      lst[ay][ax] += cnt

for l in lst: print(*list(map(lambda x:x%10, l)), sep='')
