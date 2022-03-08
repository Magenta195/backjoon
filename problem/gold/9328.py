###
# 9328. 열쇠
# problem : https://www.acmicpc.net/problem/9328
# status : solved
###
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
for _ in range(n):
  h, w = map(int, input().split())
  lst = [['.']+list(input().strip())+['.'] for _ in range(h)]
  lst = [['.']*(w+2)] + lst + [['.']*(w+2)]
  key = input().strip()
  key = '' if key == '0' else key.upper()
  visited = [[False]*(w+2) for _ in range(h+2)]
  q, lock_q = deque([]), []
  s = 0
  for i in range(h+2):
    for j in range(w+2):
      if 0<i<h+1 and 0<j<w+1 : continue
      q.append((j, i))

  while q :
    x, y = q.pop()
    for i in range(4) :
      ax = x + dx[i]
      ay = y + dy[i]
      if -1<ax<w+2 and -1<ay<h+2 and not visited[ay][ax] and lst[ay][ax] != '*':
        nxt = lst[ay][ax]
        if nxt == '$':
          s += 1
          lst[ay][ax] == '.'
          visited[ay][ax] = True
          q.append((ax, ay))
        elif nxt == '.':
          visited[ay][ax] = True
          q.append((ax, ay))
        elif nxt.isupper(): ### locked
          if nxt not in key :
            lock_q.append((nxt, ax, ay))
          else :
            lst[ay][ax] = '.'
            visited[ay][ax] = True
            q.append((ax, ay))
        else : ### get key
          key += nxt.upper()
          for lock, nx, ny in lock_q :
            if lock == key[-1] :
              lst[ny][nx] = '.'
              visited[ny][nx] = True
              q.append((nx,ny))
          lock_q = [tmp for tmp in lock_q if tmp != key[-1]] 
          lst[ay][ax] = '.'
          visited[ay][ax] = True 
          q.append((ax, ay))
  print(s)
            
