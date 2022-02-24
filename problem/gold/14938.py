###
# 14938. 서강그라운드
# problem : https://www.acmicpc.net/problem/14938
# status : solved
###
import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
item = list(map(int, input().split()))
v = [[1e10]*n for _ in range(n)]

for i in range(n): v[i][i] = 0
for a, b, l in [list(map(int, input().split())) for _ in range(r)]:
  v[a-1][b-1] = l
  v[b-1][a-1] = l
  
for k in range(n):
  for i in range(n):
    for j in range(n):
      if v[i][j] > v[i][k] + v[k][j]:
        v[i][j] = v[i][k] + v[k][j]

s = 0
for lst in v:
  tmp = 0
  for i in range(n):
    if lst[i] <= m: tmp += item[i]
  s = max(tmp, s)
print(s)
