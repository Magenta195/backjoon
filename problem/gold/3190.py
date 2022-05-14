###
# 3190. 뱀
# problem : https://www.acmicpc.net/problem/3190
# status : solved
###

dx = [1,0,-1,0]
dy = [0,1,0,-1]
dir = 0
N = int(input())
lst = [[0]*N for _ in range(N)]
lst[0][0]=-1
for _ in range(int(input())):
  y,x = map(int,input().split())
  lst[y-1][x-1]=1
L = int(input())
l_lst = [list(input().split()) for _ in range(L)]
snake,t = [(0,0)],0

while True:
  (tx,ty),hx,hy=snake[0], snake[-1][0]+dx[dir],snake[-1][1]+dy[dir]
  if hx<0 or hx>N-1 or hy<0 or hy>N-1 or lst[hy][hx] == -1 :
    print(t+1)
    exit()
  snake.append((hx,hy))
  if lst[hy][hx]==0:
    lst[ty][tx]=0
    snake.pop(0)
  lst[hy][hx]=-1
  t+=1
  if l_lst and t == int(l_lst[0][0]):
    _,r = l_lst.pop(0)
    dir = (dir+1)%4 if r == 'D' else (dir-1)%4
