  ###
  # 5213. 과외맨
  # problem : https://www.acmicpc.net/problem/5213
  # status : solved
  # time : 00:54:51
  ###
  
  import sys
from collections import deque
input = sys.stdin.readline

edx = [-1, -1, -1, 0, 1, 0]
odx = [0, -1, 0, 1, 1, 1]
dy = [-1, 0, 1, 1, 0, -1]


N = int(input())
lst = [[0]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]
m_lst = [[N**2]*N for _ in range(N)]
visited[0][0] = (0,0)
for i in range(N):
  C = N if i % 2 == 0 else N-1
  for j in range(C):
    lst[i][j] = tuple(map(int, input().split()))

q = deque([(0,0,1)])
mx, my = -1, -1

while q :
  x, y, cnt = q.popleft()
  if my < y or my == y and mx <= x :
    mx, my = x, y
    if m_lst[my][mx] > cnt : m_lst[my][mx] = cnt
    if x == y == N-1 : break

  for k in range(6):
    ay =  y+dy[k]
    ax = x+edx[k] if y % 2 == 0 else x+odx[k]
    bd = N if ay % 2 == 0 else N-1
    chk = (0, 1) if k < 3 else (1, 0)
    if -1<ax<bd and -1<ay<N and lst[y][x][chk[0]] == lst[ay][ax][chk[1]] and not visited[ay][ax] :
      visited[ay][ax] = (x, y)
      q.append((ax,ay,cnt+1))

print(m_lst[my][mx])
backtrack = [my*N+mx-(my//2)+1]
while (mx, my) != visited[my][mx] :
  mx, my = visited[my][mx]
  backtrack.append(my*N+mx-(my//2)+1)

print(*reversed(backtrack))
