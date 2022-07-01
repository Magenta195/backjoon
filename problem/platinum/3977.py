###
# 3977. 축구 전술
# problem : https://www.acmicpc.net/problem/3977
# status : solved
# time : 01:18:23
###

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())
for t in range(T):
  N, M = map(int, input().split())
  move_dict = { key : [] for key in range(N)}
  for _ in range(M):
    a, b = map(int, input().split())
    move_dict[a].append(b)
  
  visited = [-1]*N
  processed = [False]*N
  stk = deque([])
  id = 0

  scc_lst = []
  scc_id = 0
  scc_node = [-1]*N
  scc_graph = [] 
  
  def dfs(node, pre):
    global id, scc_lst, scc_id

    visited[node] = id
    id += 1
    stk.append(node)
    processed[node] = True

    p = visited[node]
    for next in move_dict[node]:
      if visited[next] == -1 :
        p = min(p, dfs(next, node))
      elif processed[next] :
        p = min(p, visited[next])
      elif scc_node[next] > -1 :
        scc_graph.append((node, next))
        
    if p == visited[node] :
      tmp = []
      while True:
        now = stk.pop()
        processed[now] = False
        tmp.append(now)
        scc_node[now] = scc_id
        if now == node : break
      scc_lst.append(tmp)
      if stk and pre != node:
        scc_graph.append((pre, node))
      scc_id += 1

    return p
  
  for i in range(N):
    if visited[i] == -1 :
      dfs(i, i)

  scc_order = [0]*scc_id
  for s, e in scc_graph :
    scc_order[scc_node[e]] += 1
  
  if scc_order.count(0) > 1 :
    print("Confused")
  else :
    print(*sorted(scc_lst[-1]), sep='\n')
    
  if t < T-1 :
    input()
    print()
