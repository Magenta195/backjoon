###
# 16235. 나무 재테크
# problem : https://www.acmicpc.net/problem/16235
# status : solved(pypy3)
###
from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, -1, -1, -1, 1, 1, 1]
dy = [-1, 1, 0, 1, -1, 0, 1, -1]
N, M, K = map(int, input().split())
e_lst = [[5]*N for _ in range(N)]
a_lst = [list(map(int,input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
  x, y, z = map(int,input().split())
  tree[x-1][y-1].append(z)
  
for _ in range(K):
  mk = deque([])
  for i in range(N):
    for j in range(N):
      if tree[i][j] :
        tree[i][j].sort()
        e = 0
        for idx, age in enumerate(tree[i][j][:]):
          if age > e_lst[i][j] :
            for age in tree[i][j][idx:]:
              e += age // 2
            tree[i][j] = tree[i][j][:idx]
            break
          e_lst[i][j] -= age
          tree[i][j][idx] = age+1
          if (age+1)% 5 == 0 :
            mk.append((i,j))
        e_lst[i][j] += e
            
  for x, y in mk :
    for i in range(8):
      ax, ay = x+dx[i], y+dy[i]
      if -1<ax<N and -1<ay<N :
        tree[ax][ay].append(1)
  for i in range(N):
    for j in range(N):
      e_lst[i][j] += a_lst[i][j]
s = 0
for i in tree:
  for j in i:
    s += len(j)
print(s)
        

