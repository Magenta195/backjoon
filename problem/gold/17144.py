###
# 17144. 미세먼지 안녕
# problem : https://www.acmicpc.net/problem/17144
# status : solved (python3 시간 초과, pypy3 통과)
###

### trial 1 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c, t = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(r)]
a = [[0]*c for _ in range(r)]

###공기청정기 찾기
for i in range(2, r-2):
  if lst[i][0] == -1 :
    ac = [i, i+1]
    break
    
for _ in range(t):
  ### 미세먼지 확산
  for i in range(r):
    for j in range(c):
      if lst[i][j] > 0:
        cnt = 0
        for k in range(4):
          x = j + dx[k]
          y = i + dy[k]
          if -1<x<c and -1<y<r and not (y in ac and x == 0): 
            a[y][x] += lst[i][j] // 5
            cnt += 1
        a[i][j] -= cnt * (lst[i][j] // 5)
  for i in range(r):
    for j in range(c):
      lst[i][j] += a[i][j]
      a[i][j] = lst[i][j]
                                
  ### 공기청정기 가동
  for i in range(1, c):
    a[0][c-i-1] = lst[0][c-i]
    a[r-1][c-i-1] = lst[r-1][c-i]
    if i != 1:
      a[ac[0]][i] = lst[ac[0]][i-1]
      a[ac[1]][i] = lst[ac[1]][i-1]
    else :
      a[ac[0]][i] = 0
      a[ac[1]][i] = 0
  
  for i in range(ac[0]):
    a[ac[0]-i][0] = lst[ac[0]-i-1][0] if i > 0 else -1
    a[i][-1] = lst[i+1][-1]
    
  for i in range(ac[1]+1, r):
    a[r-i+ac[1]-1][0] = lst[r-i+ac[1]][0] if i < r-1 else -1 
    a[i][-1] = lst[i-1][-1]

  for i in range(r):
    for j in range(c):
      lst[i][j] = a[i][j]
      a[i][j] = 0
        
print(sum(map(sum, lst))+2)
