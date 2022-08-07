###
# 17406. 배열 돌리기 4
# problem : https://www.acmicpc.net/problem/17406
# status : solved
# time : 00:21:11
###

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
query_list = [list(map(int, input().split())) for _ in range(K)]
query_order = [-1]*K

def rotate(x, y, s):
  prev = map_list[y-s][x-s]
  for i in range(x-s+1,x+s+1):
    map_list[y-s][i], prev = prev, map_list[y-s][i]
  for i in range(y-s+1,y+s+1):
    map_list[i][x+s], prev = prev, map_list[i][x+s]
  for i in range(x+s-1,x-s-1,-1):
    map_list[y+s][i], prev = prev, map_list[y+s][i]
  for i in range(y+s-1,y-s-1,-1):
    map_list[i][x-s], prev = prev, map_list[i][x-s]

def rotate_all(x, y, s):
  for _s in range(1, s+1):
    rotate(x,y,_s)

def calculate():
  result = float('inf')
  for lst in map_list :
    result = min(result, sum(lst))
  return result

def find_minval(cnt):
  global map_list
  if cnt < K :
    result = float('inf')
    for i in range(K):
      if query_order[i] == -1 :
        query_order[i] = cnt
        result = min(result, find_minval(cnt+1))
        query_order[i] = -1
    return result

  next_list = [map_list[i][:] for i in range(N)]
  for order in query_order :
    y, x, s = query_list[order]
    rotate_all(x-1,y-1,s)
  result = calculate()
  map_list = next_list
  return result
    
print(find_minval(0))
