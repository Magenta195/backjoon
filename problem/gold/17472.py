###
# 17472. 다리 만들기 2
# problem : https://www.acmicpc.net/problem/17472
# status : solved
# time : 01:09:22
###

from heapq import heappush, heappop

N, M = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[False]*M for _ in range(N)]
island_dict = dict()
island_count = 0

def dfs(x, y, idx):
  q = [(x, y)]
  island_dict[idx] = [(x,y)]
  visited[y][x] = True
  while q :
    ax, ay = q.pop()
    for k in range(4):
      bx, by = ax+dx[k],ay+dy[k]
      if -1<bx<M and -1<by<N and map_list[by][bx] == 1 and not visited[by][bx] :
        island_dict[idx].append((bx, by))
        visited[by][bx] = True
        q.append((bx, by))

def isallzero(standard, start, end, row):
  if start > end : start, end = end, start
  if row :
    return 1 in map_list[standard][start+1:end]
  else :
    lst = [map_list[x][standard] for x in range(start+1,end)]
    return 1 in lst

def find_bridge(idx1, idx2) :
  list1, list2 = island_dict[idx1], island_dict[idx2]
  length = float('inf')

  for x1, y1 in list1 :
    for x2, y2 in list2 :
      if x1 == x2 and abs(y2-y1) > 2 and not isallzero(x1, y1, y2, False):
        length = min(length, abs(y2-y1)-1)
      elif y1 == y2 and abs(x2-x1) > 2 and not isallzero(y1, x1, x2, True):
        length = min(length, abs(x2-x1)-1)

  return length if length < float('inf') else -1

def prim(edge_dict, node_num):
  mst_length = 0
  node_visited = [False]*node_num
  q = [(0, 0)]
  while q :
    dist, node = heappop(q)
    if node_visited[node] : continue
    node_visited[node] = True
    mst_length += dist
  
    for next_dist, next_node in edge_dict[node]:
      if not node_visited[next_node] : 
        heappush(q, (next_dist, next_node))

  return -1 if False in node_visited else mst_length

for i in range(N):
  for j in range(M):
    if map_list[i][j] == 1 and not visited[i][j] :
      dfs(j, i, island_count)
      island_count += 1

island_edge = { key : [] for key in range(island_count)}


for i in range(island_count-1):
  for j in range(i+1, island_count) :
    bridge_length = find_bridge(i,j)
    if bridge_length > -1 :
      island_edge[i].append((bridge_length, j))
      island_edge[j].append((bridge_length, i))

print(prim(island_edge, island_count))
      
