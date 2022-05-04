###
# 17622. 원판 돌리기
# problem : https://www.acmicpc.net/problem/17822
# status : solved
###

from collections import deque
import sys

input = sys.stdin.readline
N, M, T = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
num = N*M
for _ in range(T):
  x, d, k = map(int, input().split())
  k %= M
  ax = x
  while ax <= N :
    if k > 0 :
      lst[ax-1] = lst[ax-1][M-k:] + lst[ax-1][:M-k] if d == 0 else lst[ax-1][k:] + lst[ax-1][:k]
    ax+=x
  visited = [[False]*M for _ in range(N)]
  flg = True
  for i in range(N):
    for j in range(M):
      if not visited[i][j] and lst[i][j] > 0 :
        tmp_cnt = 1
        tmp_lst = [(j,i)]
        visited[i][j] = True
        q = deque([(j,i)])
        while q :
          x, y = q.popleft()
          for k in range(4):
            ax, ay = (x+dx[k])%M, y+dy[k]
            if -1 < ay < N and not visited[ay][ax] and lst[y][x] == lst[ay][ax] :
              visited[ay][ax] = True
              q.append((ax, ay))
              tmp_lst.append((ax, ay))
              tmp_cnt += 1
        if tmp_cnt > 1 :
          num -= tmp_cnt
          flg = False
          for x, y in tmp_lst :
            lst[y][x] = 0
  if flg and num > 0:
    avg = sum(map(sum, lst)) / num
    for i in range(N):
      for j in range(M):
        if lst[i][j] == 0 : continue
        if lst[i][j] > avg :
          lst[i][j] -= 1
        elif lst[i][j] < avg :
          lst[i][j] += 1
print(sum(map(sum, lst)))   
