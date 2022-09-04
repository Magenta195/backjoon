###
# 10021. Watering the Fields 
# problem : https://www.acmicpc.net/problem/10021
# status : solved
# time : 01:01:22
###

from heapq import heappush, heappop
import sys

input = sys.stdin.readline

N, C = map(int, input().split())
edge_lst = []
node_lst = [list(map(int, input().split())) for _ in range(N)]

def sqr_dist(a, b):
  return (a[0]-b[0])**2 + (a[1]-b[1])**2

def find(a) :
  if parent[a] == a :
    return a
  parent[a] = find(parent[a])
  return parent[a]

def union(a, b):
  pa = find(a)
  pb = find(b)
  if pa == pb :
    return False
  else :
    parent[pa] = pb
    return True

for i in range(N-1) :
  for j in range(i+1, N) :
    dist = sqr_dist(node_lst[i], node_lst[j])
    if dist >= C :
      heappush(edge_lst, (dist, i, j))

del node_lst
result = 0
edge_cnt = 0
parent = list(range(N))
while edge_lst :
  dist, a, b = heappop(edge_lst)
  if union(a, b) :
    result += dist
    edge_cnt += 1
    if edge_cnt == N-1 : break

print(result if edge_cnt == N-1 else -1)
