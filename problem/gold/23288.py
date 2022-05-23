###
# 23288. 주사위 굴리기 2
# problem : https://www.acmicpc.net/problem/23288
# status : solved
# time : 00:34:45
###

dx = [1,0,-1,0]
dy = [0,-1,0,1]

dice = [
  [0,2,0],
  [4,1,3],
  [0,5,0],
  [0,6,0]]

N, M, K = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
score_lst = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

for i in range(N):
  for j in range(M):
    if not visited[i][j] :
      visited[i][j] = True
      base,cnt = lst[i][j],1
      q = [(j,i)]
      rcd = [(j,i)]
      while q :
        x, y = q.pop(0)
        for k in range(4):
          ax, ay = x+dx[k], y+dy[k]
          if -1<ax<M and -1<ay<N and lst[ay][ax] == base and not visited[ay][ax] :
            visited[ay][ax] = True
            q.append((ax,ay))
            rcd.append((ax,ay))
            cnt += 1
      for x,y in rcd:
        score_lst[y][x] = cnt*base

x, y, dir = 0, 0, 0
score = 0
for _ in range(K):
  if not (-1 < x+dx[dir] < M and -1 < y+dy[dir] < N ) :
    dir = (dir+2)%4
  x, y = x+dx[dir], y+dy[dir]
  if dir == 0 :
    dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
  elif dir == 3 :
    dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
  elif dir == 2 :
    dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
  else :
    dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]

  score += score_lst[y][x]
  if lst[y][x] < dice[3][1] :
    dir = (dir-1)%4
  elif lst[y][x] > dice[3][1] :
    dir = (dir+1)%4
print(score)
