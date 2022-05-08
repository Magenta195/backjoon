###
# 15685. 드래곤 커브
# problem : https://www.acmicpc.net/status?user_id=magenta&problem_id=15685&from_mine=1
# status : solved

import sys

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N = int(input())
v_lst = [[False]*101 for _ in range(101)]

for i in range(N):
  x, y, d, g = map(int, input().split())
  d = [d]
  for _ in range(g):
    d += [(i+1)%4 for i in reversed(d)]
  v_lst[y][x] = True
  for j in d:
    x, y = x + dx[j], y + dy[j]
    v_lst[y][x] = True

cnt = 0
for i in range(100):
  for j in range(100):
    if v_lst[i][j] and v_lst[i][j+1] and v_lst[i+1][j] and v_lst[i+1][j+1] :
      cnt += 1
print(cnt)
  
