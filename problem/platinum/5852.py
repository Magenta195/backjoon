###
# 5852. Island Travels
# problem : https://www.acmicpc.net/problem/5852
# status : solved(pypy3)
# time : 00:58:52
###

import sys
from collections import defaultdict, deque

input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
MAX = float('inf')

R, C = map(int, input().split())
map_list = [input().strip() for _ in range(R)]
island_cnt = 0
island_dict = defaultdict(set)

visited = [[False]*C for _ in range(R)]
for i in range(R) :
  for j in range(C) :
    if map_list[i][j] == 'X' and not visited[i][j] :
      visited[i][j] = True
      q = deque([(i, j)])
      coord_set = set([(i, j)])
      while q :
        y, x = q.pop()
        for k in range(4):
          ax, ay = x+dx[k], y+dy[k]
          if -1<ax<C and -1<ay<R and map_list[ay][ax] == 'X' and not visited[ay][ax] :
            visited[ay][ax] = True
            q.append((ay, ax))
            coord_set.add((ay, ax))
      island_dict[island_cnt] = coord_set
      island_cnt += 1

edge_mat = [[MAX]*island_cnt for _ in range(island_cnt)]

for i in range(island_cnt-1) :
  visited = [[False]*C for _ in range(R)]
  q = deque([(0, y, x) for y, x in island_dict[i]])
  while q :
    dist, y, x = q.popleft()
    for k in range(4) :
      ax, ay = x+dx[k], y+dy[k]
      if -1<ax<C and -1<ay<R :
        if map_list[ay][ax] == 'S' and not visited[ay][ax] :
          visited[ay][ax] = True
          q.append((dist+1, ay, ax))
        elif map_list[ay][ax] == 'X' and (ay, ax) not in island_dict[i] :
          for j in range(i+1, island_cnt) :
            if (ay, ax) in island_dict[j] :
              edge_mat[i][j] = edge_mat[j][i] = min(edge_mat[i][j], dist)

dp = [[MAX]*island_cnt for _ in range(1 << island_cnt)]
for i in range(1 << island_cnt) :
  for j in range(island_cnt) :
    if i | (1 << j) == (1 << j) :
      dp[i][j] = 0
    for k in range(island_cnt) :
      dp[i | (1 << k)][k] = min(dp[i | (1 << k)][k], dp[i][j] + edge_mat[j][k])

print(min(dp[-1]))
