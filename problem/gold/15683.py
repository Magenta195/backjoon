###
# 15683. 감시
# problem : https://www.acmicpc.net/problem/15683
# status : solved
###
import sys
input = sys.stdin.readline
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def solve(cnt, watch_lst):
  global ans, cctv, unwatch
  if cnt < cctv :
    typ = v_lst[cnt][-1]
    if typ == 5 :
      solve(cnt+1, watch_lst+[0])
    elif typ == 2 :
      for i in range(2):
        solve(cnt+1, watch_lst+[i])
    else : 
      for i in range(4):
        solve(cnt+1, watch_lst+[i])
    return
  
  visited = [[False]*M for _ in range(N)]
  tmp = 0
  def watch(x, y, i):
    cnt = 0
    while -1<x<M and -1<y<N and lst[y][x] != 6 :
      if not visited[y][x] :
        visited[y][x] = True
        cnt += 1
      x, y = x+dx[i], y+dy[i]
    return cnt
    
  for i, (x, y, typ) in enumerate(v_lst):
    dir = watch_lst[i]
    if typ == 1 :
      tmp += watch(x, y, dir)
    elif typ == 2 :
      tmp += watch(x, y, dir) + watch(x, y, dir+2)
    elif typ == 3 :
      tmp += watch(x, y, dir) + watch(x, y, (dir+1)%4)
    elif typ == 4 :
      tmp += watch(x, y, dir) + watch(x, y, (dir+1)%4) + watch(x, y, (dir+2)%4)
    else : 
      for j in range(4):
        tmp += watch(x, y, (dir+j)%4)
    ans = min(ans, max(0, unwatch - tmp))
   

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
v_lst = []
ans = N*M + 1
unwatch, cctv = 0, 0

for i in range(N):
  for j in range(M):
    if 0 < lst[i][j] < 6 :
      v_lst.append((j,i,lst[i][j]))
      cctv += 1
      unwatch += 1
    elif lst[i][j] == 0 :
      unwatch += 1

if unwatch == 0 or unwatch == cctv :
  print(0)
elif cctv == 0:
  print(unwatch)
else :
  solve(0, [])
  print(ans)
