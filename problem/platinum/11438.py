###
# 11438. LCA 2
# problem : https://www.acmicpc.net/problem/11438
# status : solved(pypy3)
###

import sys
from collections import deque
input = sys.stdin.readline
MAX = 21

def parent_check():
  while q :
    n = q.popleft()
    depth = d[n]
    for i in tree[n]:
      if d[i] == -1:
        d[i] = depth + 1
        p[i][0] = n
        q.append(i)
    
  for i in range(1, MAX):
    for j in range(1, N+1):
      p[j][i] = p[p[j][i-1]][i-1]

N = int(input())
tree = [[] for _ in range(N+1)]
p = [[0]*MAX for i in range(N+1)]
d = [-1]*(N+1)
q = deque([1])
d[1] = 0
p[1][0] = 1

for _ in range(N-1):
  a, b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

parent_check()
M = int(input())
for _ in range(M):
  a, b = map(int, input().split())
  
  if d[a] < d[b] : a,b = b,a
  diff = d[a] - d[b]
  
  for i in range(MAX-1, -1, -1):
    if diff & (1 << i): 
      a = p[a][i]
      
  if a == b :
    print(a)
    continue
  
  for i in range(MAX-1, -1, -1):
    if p[a][i] != p[b][i]:
      a, b = p[a][i], p[b][i]
  
  print(p[a][0])

  
