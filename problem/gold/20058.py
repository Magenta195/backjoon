###
# 20058. 마법사 상어와 파이어스톰
# problem : https://www.acmicpc.net/problem/20058
# time : 00:42:48
# status : solved
###

from collections import deque
import sys
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

input = sys.stdin.readline
N, Q = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(2**N)]

def rotate(x, y, l):
  global lst
  tmp = [[lst[i][j] for i in range(y+l-1, y-1, -1)] for j in range(x, x+l)]
  for i in range(l):
    for j in range(l):
      lst[y+i][x+j] = tmp[i][j]

l_lst = list(map(int,input().split()))

for l in l_lst :
  for i in range(0, 2**N, 2**l):
    for j in range(0, 2**N, 2**l):
      rotate(i,j,2**l)
  m = deque([])
  for i in range(2**N):
    for j in range(2**N):
      if lst[i][j] == 0 : continue
      cnt = 0
      for k in range(4):
        ax, ay = j+dx[k], i+dy[k]
        if -1<ax<2**N and -1<ay<2**N and lst[ay][ax] > 0: cnt +=1
      if cnt < 3:
        m.append((j,i))
  for x, y in m :
    lst[y][x] = max(lst[y][x]-1, 0)


s, ans = 0, 0
visited = [[False]*(2**N) for _ in range(2**N)]
for i in range(2**N):
  for j in range(2**N):
    if lst[i][j] > 0 and not visited[i][j]:
      cnt = 1
      visited[i][j] = True
      s += lst[i][j]
      q = deque([(j,i)])
      while q :
        x, y = q.popleft()
        for k in range(4):
          ax, ay = x+dx[k], y+dy[k]
          if -1<ax<2**N and -1<ay<2**N and not visited[ay][ax] and lst[ay][ax] > 0:
            visited[ay][ax] = True
            s += lst[ay][ax]
            q.append((ax,ay))
            cnt += 1
      ans = max(ans, cnt)

print(s)
print(ans)
