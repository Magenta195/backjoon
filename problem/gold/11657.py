###
# 11657. 타임머신
# problem : https://www.acmicpc.net/problem/11657
# status : solved
# time : 00:21:59
###

from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
MAX = float('inf')
lst = []
dist = [MAX]*N
for _ in range(M):
  a,b,c = map(int,input().split())
  lst.append((a-1,b-1,c))

def bf():
  dist[0] = 0
  for i in range(N+1):
    for s, e, d in lst:
      if dist[s] < MAX and dist[e] > dist[s]+d:
        dist[e] = dist[s] + d
        if i == N : return True
  return False

if bf() : print(-1)
else : print(*[x if x < MAX else -1 for x in dist][1:], sep = '\n')
