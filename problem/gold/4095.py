###
# 4095. 최대 정사각형
# problem : https://www.acmicpc.net/problem/4095
# status : solved
###

import sys
input = sys.stdin.readline

while True :
  N, M = map(int, input().split())
  if N == M == 0 : break
  
  lst = [[*map(int, input().split())] for _ in range(N)]
  
  ans = 0
  for i in range(N):
    for j in range(M):
      if lst[i][j] == 1 :
        if 0 < i and 0 < j :
          lst[i][j] = min(lst[i-1][j], lst[i][j-1], lst[i-1][j-1])+1
        ans = max(lst[i][j], ans)

  print(ans)
