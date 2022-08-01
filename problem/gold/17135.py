###
# 17135. 캐슬 디펜스
# problem : https://www.acmicpc.net/problem/17135
# status : solved
###

from itertools import combinations
import sys
input = sys.stdin.readline

N, M, D = map(int, input().split())
dx = [-1,0,1]
dy = [0,-1,0]
initial_map = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for archers in combinations(range(M), 3):
  current_map = [lst[:] for lst in initial_map]
  removed = 0
  for _ in range(N) :
    remove_set = set()
    for archer in archers :
      q = [(1, archer, N-1)]
      visited = [[False]*M for _ in range(N)]
      visited[N-1][archer] = True
      while q:
        dist, x, y = q.pop(0)
        if dist > D : continue
        if current_map[y][x] == 1 :
          remove_set.add((x,y))
          break

        for k in range(3):
          ax, ay = x+dx[k], y+dy[k]
          if -1<ax<M and -1<ay<N and not visited[ay][ax] :
            visited[ay][ax] = True
            q.append((dist+1,ax,ay))

    removed += len(remove_set)
    for x, y in remove_set :
      current_map[y][x] = 0
    current_map = [[0]*M] + current_map[:-1]
  
  answer = max(answer, removed)
print(answer)
