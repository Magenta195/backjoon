###
# 1202. 보석 도둑
# problem : https://www.acmicpc.net/problem/1202
# status :
###
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())
n_lst = []
for _ in range(n) :
  heappush(n_lst, list(map(int, input().split())))
c = sorted([int(input()) for _ in range(k)])

s = 0
tmp = []
for i in c:  
  while n_lst and n_lst[0][0] <= i :
    heappush(tmp, -heappop(n_lst)[1])
  if tmp :
    s -= heappop(tmp)
  elif not n_lst : break
print(s)
