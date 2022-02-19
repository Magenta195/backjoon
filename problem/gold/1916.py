###
# 1916. 테트로미노
# problem : https://www.acmicpc.net/problem/1916
# status : solved
### 
### non-priority queue ver
### time complexity : o(V^2)

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
e = [[1e10]*n for _ in range(n)]
for _ in range(m) :
  i, o, v = map(int, input().split())
  e[i-1][o-1] = min(e[i-1][o-1], v)
i, o = map(int, input().split())

q = list(range(n))
v = [0]*n
e[i-1][i-1] = 0

while q:
  q.sort(key = lambda x : e[i-1][x])
  k = q.pop(0)
  
  for j in range(n):
    if e[i-1][j] > e[i-1][k] + e[k][j] :
      e[i-1][j] = e[i-1][k] + e[k][j]

print(e[i-1][o-1])
