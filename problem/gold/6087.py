###
# 6087. 레이저 통신
# problem : 
# status :
###

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
w, h = map(int, input().split())
lst = [input().strip() for _ in range(h)]
q = []

flg = True
for i in range(h):
  for j in range(w):
    if lst[i][j] == 'C' :
      if flg :
        start = (j,i)
        for k in range(4):
          ax, ay = j+dx[k], i+dy[k]
          if -1<ax<w and -1<ay<h and lst[ay][ax] != '*': 
            q.append((0,ax,ay,k))
        flg = False
      else : end = (j,i)
        
visited = [[[False]*w for _ in range(h)] for _ in range(4)]
for _, ax, ay, k in q:
  visited[k][start[1]][start[0]] = True
  visited[k][ay][ax] = True

while q:
  crv, x, y, dir = heappop(q)
  if (x,y) == end :
    print(crv)
    break
  for i in [-1,0,1]:
    ad = (dir+i)%4
    ax, ay = x+dx[ad], y+dy[ad]
    if -1<ax<w and -1<ay<h and lst[ay][ax] != '*' and not visited[ad][ay][ax]:
      visited[ad][ay][ax] = True
      heappush(q, (crv,ax,ay,ad) if i == 0 else (crv+1,ax,ay,ad))
