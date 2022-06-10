###
# 1981. 배열에서 이동
# problem : https://www.acmicpc.net/problem/1981
# status : solved
# time : 00:55:01
###

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

def bfs(l,r):
  if not l <= lst[0][0] <= r : return False 
  q = deque([(0,0)])
  visited = [[False]*N for _ in range(N)]
  visited[0][0] = True
  while q :
    x, y = q.popleft()
    if x == y == N-1:
      return True
  
    for i in range(4):
      ax, ay = x+dx[i], y+dy[i]
      if -1<ax<N and -1<ay<N and l <= lst[ay][ax] <= r and not visited[ay][ax] :
        visited[ay][ax] = True
        q.append((ax,ay))
  return False

l, r, ans = 0, 0, 201
while l < 201 and r < 201:
  if bfs(l,r) :
    ans = min(ans, r-l)
    l += 1
  else :
    r += 1
    
print(ans)
