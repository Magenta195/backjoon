###
# 2252. 줄 세우기
# problem : https://www.acmicpc.net/problem/2252
# status : solved
###
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = { key : [] for key in range(1, n+1)}
lst = [0]*(n+1)
q = []
for a, b in [list(map(int,input().split())) for _ in range(m)]:
  g[a].append(b)
  lst[b] += 1

for i in range(1, n+1):
  if lst[i] == 0 : q.append(i)
    
while q:
  i = q.pop(0)
  print(i, sep=' ')
  for j in g[i]:
    lst[j] -= 1
    if lst[j] == 0 : q.append(j)
