###
# 17780. 새로운 게임
# problem : https://www.acmicpc.net/problem/17780
# status : solved
# time : ?????
###


from collections import *
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]
rev = [0, 2, 1, 4, 3]

N, K = map(int,input().split())
lst = [[2]*(N+2)] + [[2]+list(map(int,input().split()))+[2] for _ in range(N)] + [[2]*(N+2)]
horse = []
map_lst = [[deque([]) for _ in range(N+2)] for _ in range(N+2)]
for i, (y, x, dir) in enumerate([list(map(int,input().split())) for _ in range(K)]):
  horse.append([x,y,dir])
  map_lst[y][x].append(i)

for i in range(1000):
  for j, (x, y, dir) in enumerate(horse):
    if map_lst[y][x][0] != j : continue
    ax, ay = x+dx[dir], y+dy[dir]
    
    if lst[ay][ax] == 2 :
      dir = rev[dir]
      ax, ay = x+dx[dir], y+dy[dir]
      if lst[ay][ax] == 2:
        horse[j] = [x, y, dir]
        continue
    tmp_lst = deque([])
    while True :
      k = map_lst[y][x].pop()
      horse[k][0], horse[k][1] = ax, ay
      tmp_lst.appendleft(k)
      if k == j : 
        horse[k][2] = dir
        break
    if lst[ay][ax] == 1 :
      tmp_lst.reverse()
    map_lst[ay][ax].extend(tmp_lst)
    if len(map_lst[ay][ax]) >= 4 :
      print(i+1)
      exit()
print(-1)
