###
# 13977. 이항 계수와 쿼리
# problem : https://www.acmicpc.net/problem/13977
# status : solved
###

import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
num =  1000000007
fac = [1]*4000001

def pow(n,k):
  if k == 1:
    return n

  a = pow(n, k//2) % num
  a = (a**2) % num
  if k % 2 == 0:
    return a
  else :
    return (a * (n % num)) % num

for i in range(2, 4000001):
  fac[i] = (fac[i-1]*i) % num
  
m = int(input())
for _ in range(m):
  n, k = map(int,input().split())
  ans = (fac[n] * pow((fac[k]*fac[n-k]) % num,num-2)) % num
  print(ans)
