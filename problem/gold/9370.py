###
# 9370. 미확인 도착지
# problem : https://www.acmicpc.net/problem/9370
# status : solved
# time : 00:42:45
###

from heapq import heappush, heappop
import sys

input = sys.stdin.readline
INF = float('inf')
for _ in range(int(input())):
  n, m, t = map(int, input().split())
  s, g, h = map(int, input().split())

  dic = { keys : [] for keys in range(n)}
  for _ in range(m):
    a, b, d = map(int,input().split())
    if (a,b) == (g,h) or (b,a) == (g,h) :
      dic[a-1].append((b-1,d-0.1))
      dic[b-1].append((a-1,d-0.1))
    else :
      dic[a-1].append((b-1,d))
      dic[b-1].append((a-1,d))

  d_mat = [INF]*n
  d_mat[s-1] = 0
  q = [(0,s-1)]

  while q :
    dist, start = heappop(q)
    if d_mat[start] < dist : continue
    for end, new_d in dic[start] :
      if d_mat[end] > dist + new_d :
        d_mat[end] = dist + new_d
        heappush(q, (dist+new_d, end))

  ans = []
  for _ in range(t):
    x = int(input())
    if d_mat[x-1] < INF and type(d_mat[x-1]) == float :
      ans.append(x)
  print(*sorted(ans))
