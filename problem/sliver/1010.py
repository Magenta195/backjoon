###
# 1010. 다리 놓기
# problem : https://www.acmicpc.net/problem/1010
# status : solved
###

import sys

MAX = 30
input = sys.stdin.readline
N = int(input())

factorial = [1]*(MAX+1)
for i in range(2, MAX+1):
  factorial[i] = factorial[i-1]*i

for _ in range(N):
  a, b = map(int, input().split())
  print(int(factorial[b] / (factorial[a] * factorial[b-a])))
