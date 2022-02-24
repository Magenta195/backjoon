###
# 11779. 최소비용 구하기 2
# problem : https://www.acmicpc.net/problem/11779
# status : solved
###
import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
v = { key : [] for key in range(1, n+1) }
for s, e, t in [list(map(int, input().split())) for _ in range(m)]:
  v[s].append((e,t))
s, e = map(int, input().split())

d_lst = [[1e10,''] for _ in range(n+1)]
d_lst[s][0] = 0
d_lst[s][1] += str(s)
q = [(0, s)]

while q:
  d, i = heapq.heappop(q)
  if d_lst[i][0] < d : continue
  for nd, t in v[i]:
    if d + t < d_lst[nd][0]:
      d_lst[nd][0] = d + t
      d_lst[nd][1] = d_lst[i][1]+','+str(nd)
      heapq.heappush(q, (d + t, nd))

lst = list(map(int, d_lst[e][1].split(',')))
print(d_lst[e][0], len(lst), sep='\n')
print(*lst)
