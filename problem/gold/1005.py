###
# 1005. ACM Craft
# problem : https://www.acmicpc.net/problem/1005
# status :solved
###
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dp(node, graph, lst):
  if not graph[node] :
    lst[node-1] = 0
    return 0
  
  cnt = 0
  if lst[node-1] == 1e11 :
    for i, t in graph[node] :
      cnt = max(cnt, dp(i, graph, lst) + t)
    lst[node-1] = cnt
  else : cnt = lst[node-1]
  return cnt

for _ in range(int(input())):
  n, k = map(int, input().split())
  d = list(map(int, input().split()))
  g = { key : [] for key in range(1, n+1) }
  for x, y in [list(map(int, input().split())) for _ in range(k)]:
    g[y].append((x, d[x-1]))
  w = int(input())
  lst = [1e11]*n
  print(dp(w, g, lst) + d[w-1])
