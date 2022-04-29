###
# 14503. 로봇 청소기
# problem : https://www.acmicpc.net/problem/14503
# status : solved
###

import sys
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N, M = map(int, input().split())
y, x, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
cnt = 0
while True:
  visited[y][x] = True
  cnt += 1
  rotate = 0
  while True:
    d = (d - 1) % 4
    ax, ay = x + dx[d], y + dy[d]
    if lst[ay][ax] == 0 and not visited[ay][ax]:
      x, y = ax, ay
      break
    rotate += 1
    if rotate == 4 :
      if lst[y-dy[d]][x-dx[d]] == 1:
        print(cnt)
        exit()
      else :
        x, y = x-dx[d], y-dy[d]
        rotate = 0
