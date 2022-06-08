###
# 17435. 합성함수와 쿼리
# problem : https://www.acmicpc.net/problem/17435
# status : solved 
# time : 00:17:09
###

import sys
input = sys.stdin.readline

MAX = 20
M = int(input())
m_lst = [0]+list(map(int,input().split()))
mat = [[-1]*(M+1) for _ in range(MAX)]

for i in range(MAX):
  for j in range(1,M+1):
    if i == 0 :
      mat[i][j] = m_lst[j]
    else :
      mat[i][j] = mat[i-1][mat[i-1][j]]

for _ in range(int(input())):
  n, x = map(int,input().split())

  for i in range(MAX):
    if (1 << i) & n :
      x = mat[i][x]
  print(x)
