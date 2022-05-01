###
# 19238. 스타트 택시
# problem : https://www.acmicpc.net/problem/19238
# status : solved (pypy3)
###
from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M, fuel = map(int, input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
ty, tx = map(int, input().split())
tx, ty = tx-1, ty-1
guest_lst = [[x-1 for x in map(int, input().split())] for _ in range(M)]
while guest_lst:
  visited = [[False]*N for _ in range(N)]
  visited[ty][tx] = True
  q = deque([(0, tx, ty)])
  MAX = N*N+1
  tmp_lst = []
  while q:
    dist, x, y = q.popleft()
    for i, (Sy, Sx, Ey, Ex) in enumerate(guest_lst):
      if Sx == x and Sy == y :
        tmp_lst.append((Sx,Sy,dist,i))
    for i in range(4):
      ax, ay = x+dx[i], y+dy[i]
      if -1<ax<N and -1<ay<N and lst[ay][ax] == 0 and not visited[ay][ax]:
        visited[ay][ax] = True
        q.append((dist+1, ax, ay))

  tmp_lst.sort(key=lambda x :(x[2], x[1], x[0]))
  if not tmp_lst or fuel < tmp_lst[0][2]:
    print(-1)
    exit()

  fuel -= tmp_lst[0][2]
  ty, tx, Dy, Dx = guest_lst.pop(tmp_lst[0][-1])
  visited = [[False]*N for _ in range(N)]
  visited[ty][tx] = True
  q = deque([(0, tx, ty)])
  flg = False
  while q:
    dist, x, y = q.popleft()
    if x == Dx and y == Dy : 
      flg = True
      break
    for i in range(4):
      ax, ay = x+dx[i], y+dy[i]
      if -1<ax<N and -1<ay<N and lst[ay][ax] == 0 and not visited[ay][ax] :
        visited[ay][ax] = True
        q.append((dist+1, ax, ay))
  if fuel < dist or not flg:
    print(-1)
    exit()
  fuel += dist
  tx, ty = x, y

print(fuel)
       
