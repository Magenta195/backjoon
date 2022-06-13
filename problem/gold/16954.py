###
# 16954. 움직이는 미로 탈출
# problem : https://www.acmicpc.net/problem/16954
# status : solved
###

from collections import deque

dx = [0, 0, 0, 1, 1, 1, -1, -1, -1]
dy = [0, 1, -1, 1, 0, -1, 1, 0, -1]

lst = [[input().strip() for _ in range(8)]]
for _ in range(8):
  tmp = ['.'*8] + lst[-1][:-1]
  lst.append(tmp)

q = deque([(0,7,0)])
visited = [[[False]*8 for _ in range(8)] for _ in range(9)]
while q :
  x, y, t = q.popleft()
  if x == 7 and y == 0 :
    print(1)
    exit()
  for i in range(9):
    ax, ay = x+dx[i], y+dy[i]
    if -1<ax<8 and -1<ay<8 :
      if t < 8 and lst[t][ay][ax] != '#' and lst[t+1][ay][ax] != '#' and not visited[t+1][ay][ax]:
        visited[t+1][ay][ax] = True
        q.append((ax,ay,t+1))
      elif t == 8 and not visited[-1][ay][ax] :
        visited[-1][ay][ax] = True
        q.append((ax,ay,t))
      
print(0)
