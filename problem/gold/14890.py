###
# 14890. 경사로
# problem : https://www.acmicpc.net/problem/14890
# status : solved
###

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

for i in range(N):
  j = 0
  comp = False
  visited = [False]*N
  while j < N-1:
    now, next = lst[i][j], lst[i][j+1]
    if now == next :
      j += 1
    elif now == next+1 :
      if j + L >= N : break
      else :
        flg = False
        for k in range(j+1, j+L+1):
          visited[k] = True
          if lst[i][k] != next :
            flg = True
            break
        if flg : break
        j += L
    elif now == next-1:
      if j - L + 1 < 0: break
      else :
        flg = False
        for k in range(j,j-L,-1):
          if lst[i][k] != now or visited[k] :
            flg = True
            break
        if flg : break
        j += 1
    else : break
    if j == N-1 : comp = True
  if comp : cnt += 1

for i in range(N):
  j = 0
  comp = False
  visited = [False]*N
  while j < N-1:
    now, next = lst[j][i], lst[j+1][i]
    if now == next :
      j += 1
    elif now == next+1 :
      if j + L >= N : break
      else :
        flg = False
        for k in range(j+1, j+L+1):
          visited[k] = True
          if lst[k][i] != next :
            flg = True
            break
        if flg : break
        j += L
    elif now == next-1:
      if j - L + 1< 0 or visited[j] : break
      else :
        flg = False
        for k in range(j,j-L,-1):
          if lst[k][i] != now or visited[k] :
            flg = True
            break
        if flg : break
        j += 1
    else : break
    if j == N-1 : comp = True
  if comp : cnt += 1
    
print(cnt)
        
   
