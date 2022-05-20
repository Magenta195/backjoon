###
# 20057. 마법사 상어와 토네이도
# problem : https://www.acmicpc.net/problem/20057
# status : solved
###

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
tx, ty = N//2, N//2
t_map = [list(map(int,input().split())) for _ in range(N)]
out = 0
t_range = [
  (-1,1,1), (-1,-1,1),
  (0,2,2),(0,1,7),(0,-1,7),(0,-2,2),
  (1,1,10),(1,-1,10),
  (2,0,5),(1,0,0)]

def move(x,y,dir):
  global out, t_map
  total = t_map[y][x]
  if total == 0 : return
  for i,j,mul in t_range:
    ax, ay = (x+dx[dir]*i, y+j) if dir%2 == 0 else (x+j, y+dy[dir]*i)
    if mul > 0:
      mvd = t_map[y][x] * mul // 100
      if -1 < ay < N and -1 < ax < N :
        t_map[ay][ax] += mvd
        
      else :
        out += mvd
      total -= mvd
    else :
      if -1 < ay < N and -1 < ax < N :
        t_map[ay][ax] += total
      else :
        out += total
  
  t_map[y][x] = 0

cnt, dir = 1, 0

while True :
  for _ in range(cnt):
    tx, ty = tx+dx[dir],ty+dy[dir]
    move(tx,ty,dir)
    if tx == ty == 0 : break
  if tx == ty == 0 : break
  dir = (dir+1)%4
  for _ in range(cnt):
    tx, ty = tx+dx[dir],ty+dy[dir]
    move(tx,ty,dir)
  dir = (dir+1)%4
  cnt += 1
print(out)
