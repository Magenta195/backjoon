###
# 21610. 마법사 상어와 비바라기
# problem : https://www.acmicpc.net/problem/21610
# time : 00:44:35
# status : solved
###

import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
Dx = [-1, -1, 1, 1]
Dy = [1, -1, -1, 1]

N, M = map(int, input().split())
cloud = [[0, N-1], [0, N-2], [1, N-1], [1, N-2]]
lst = [list(map(int, input().split())) for _ in range(N)]

for _ in range(M):
  d, s = map(int, input().split())
  t_lst = [[0]*N for _ in range(N)]
  for x, y in cloud :
    x, y = (x+s*dx[d-1])%N, (y+s*dy[d-1])%N
    t_lst[y][x] = 1

  tmp = []
  for i in range(N):
    for j in range(N):
      if lst[i][j] >= 2 and t_lst[i][j] == 0 :
        lst[i][j] -= 2
        tmp.append([j,i])
      elif t_lst[i][j] > 0 :
        cnt = 0
        for k in range(4):
          ax, ay = j+Dx[k], i+Dy[k]
          if -1<ax<N and -1<ay<N and (lst[ay][ax] > 0 or t_lst[ay][ax] > 0 or [ax, ay] in tmp): cnt += 1
        lst[i][j] += cnt + t_lst[i][j]
  cloud = tmp
print(sum(map(sum, lst)))
