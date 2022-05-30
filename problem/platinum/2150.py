###
# 2150. Stroingly Connectied Component
# problem : 
# status :
# time : ???
###

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
V, E = map(int, input().split())

id = 0
dic = {keys : [] for keys in range(1,V+1)}
p = [0]*(V+1)
finished = [False]*(V+1)

for _ in range(E):
  a, b = map(int,input().split())
  dic[a].append(b)

scc, stk = [],[]
def dfs(x):
  global scc, stk, id
  id += 1
  p[x] = id
  stk.append(x)
  parent = p[x]
  
  for i in dic[x]:
    if p[i] == 0 :
      parent = min(parent, dfs(i))
    elif not finished[i] :
      parent = min(parent, p[i])
  
  if parent == p[x] :
    tmp = []
    while True :
      t = stk.pop()
      finished[t] = True
      tmp.append(t)
      if t == x : break
    scc.append(sorted(tmp))
  
  return parent
  
for i in range(1,V+1):
  if not finished[i] : dfs(i)
scc.sort()
print(len(scc))
for s in scc:
  print(*s, -1)
