###
# 11400. 단절선
# problem : https://www.acmicpc.net/problem/11400
# status : solved
###

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e7))
V, E = map(int, input().split())
v_search = [0]*(V+1)
edge_lst = []
num = 0

e = { keys : [] for keys in range(1, V+1)}
for _ in range(E):
  a, b = map(int, input().split())
  e[a].append(b)
  e[b].append(a)

def dfs(node, parent):
  global num
  num += 1
  v_search[node] = num
  ret = num
  
  for next in e[node] :
    if next == parent : continue
    
    if v_search[next] > 0 :
      ret = min(ret, v_search[next])
      continue
      
    subtree = dfs(next, node)
    ret = min(subtree, ret)
    if subtree > v_search[node] :
      edge_lst.append(sorted([node, next]))
  return ret

dfs(1,1)
edge_lst.sort(key = lambda x : (x[0], x[1]))

print(len(edge_lst))
for a, b in edge_lst:
  print(a,b)
