###
# 9471. 피사노 주기
# problem : https://www.acmicpc.net/problem/9471
# status : solved
###

P = int(input())
for _ in range(P):
  N,M=map(int,input().split())
  a,b,c=1,1,1
  while (a,b)!=(0,1):
    a,b,c=(a+b)%M,a,c+1
  print(N,c)
