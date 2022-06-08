###
# 4991. 로봇 청소기
# problem : https://www.acmicpc.net/problem/4991
# status : solved
# time : 00:09:48
###

from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
while True :
  w, h = map(int, input().split())
  if w == h == 0 : break

  lst = [input().strip() for _ in range(h)]
  trash = []
  cnt = 0
  for i in range(h):
    for j in range(w):
      if lst[i][j] == '*' :
        trash.append((j,i))
        cnt += 1
      elif lst[i][j] == 'o' :
        sx, sy = j, i
  if cnt == 0 :
    print(0)
    break
  visited = [[[False]*w for _ in range(h)] for _ in range(2**cnt)]
  visited[0][sy][sx] = True
  q = deque([(sx,sy,0,0)])
  flg = False

  while q :
    x, y, v, c = q.popleft()
    if v == 2**cnt-1 :
      flg = True
      break
    for i in range(4):
      ax, ay, av = x+dx[i],y+dy[i], v
      if -1 < ax < w and -1 < ay < h and lst[ay][ax] != 'x' :
        if lst[ay][ax] == '*' :
          num = trash.index((ax, ay))
          av = av | (1 << num)
        if visited[av][ay][ax] : continue
        visited[av][ay][ax] = True
        q.append((ax,ay,av,c+1))
  print(c if flg else -1)
