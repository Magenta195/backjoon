###
# 1533. 길의 개수
# problem : https://www.acmicpc.net/problem/1533
# status : solved
###


import sys
input = sys.stdin.readline
MOD = 1000003

def matmul(a, b):
  tmp = [[0]*(5*N) for _ in range(5*N)]
  for i in range(5*N):
    for j in range(5*N):
      for k in range(5*N):
        tmp[i][j] += a[i][k]*b[k][j] % MOD
      tmp[i][j] %= MOD
  return tmp

def matpow(a, n):
  if n == 1:
    return a
  p = matpow(a, n//2)
  p = matmul(p,p)
  
  if n % 2 == 0 : return p
  else :
    return matmul(p, a)

N,S,E,T = map(int, input().split())
raw_lst = [list(map(int,list(input().strip()))) for _ in range(N)]
lst = [[0]*(5*N) for _ in range(5*N)]

for i in range(N):
  for j in range(1,5):
    lst[5*i+j][5*i+j-1] = 1
for i in range(N):
  for j in range(N):
    K = raw_lst[i][j]
    if K > 0:
      lst[5*i][5*j+K-1] = 1
f_lst = matpow(lst, T)
print(f_lst[5*(S-1)][5*(E-1)])
