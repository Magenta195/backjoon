###
# 16568. 엔비스카의 영혼
# problem : https://www.acmicpc.net/problem/16568
# status : solved
###
from heapq import heappush, heappop

N, a, b = map(int, input().split())
if N == 0 : 
  print(0)
  exit()
action = [1, 1+a, 1+b]
dp = [-1]*(N+1)

q = [(0, N)]

while q :
  cnt, num = heappop(q)
  for i in action :
    if num - i < 0 or dp[num-i] > -1: continue
    elif num - i == 0:
      print(cnt+1)
      exit()
    dp[num-i] = cnt+1
    heappush(q, (cnt+1, num-i))
  
