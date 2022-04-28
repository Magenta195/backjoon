###
# 14499. 주사위 굴리기
# problem : https://www.acmicpc.net/problem/14499
# status : solved
###

dice = [[0]*3 for _ in range(4)]
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]

N, M, y, x, K = map(int, input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
for i in list(map(int, input().split())) :
  ax, ay = x + dx[i], y + dy[i]
  if -1 < ax < M and -1 < ay < N :
    x, y = ax, ay
    if i == 1 :
      dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
    elif i == 2 : 
      dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
    elif i == 3 :
      dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
    else : 
      dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
    if lst[ay][ax] == 0:
      lst[ay][ax] = dice[3][1]
    else :
      dice[3][1] = lst[ay][ax]
      lst[ay][ax] = 0
    print(dice[1][1])
  
