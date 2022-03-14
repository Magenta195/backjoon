###
# 16724. 피리 부는 사나이
# problem : https://www.acmicpc.net/problem/16724
# status : not solved
###
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100)

n, m = map(int, input().split())
lst = [input().strip() for _ in range(n)]
parent = [[(x,y) for x in range(m)] for y in range(n)]
v = [[False]*m for _ in range(n)]

for i in range(n):
  for j in range(m):
    ch = lst[i][j]
    if ch == 'U' : parent[i][j] = (j, i-1)
    elif ch == 'D' : parent[i][j] = (j, i+1)
    elif ch == 'R' : parent[i][j] = (j+1, i)
    else : parent[i][j] = (j-1, i)

print(parent)
def find(x, y):
  print(x,y)
  print(parent[y][x])
  v[x][y] = True
  print(v)
  if parent[y][x] == (x,y) :
    return x, y
  if v[parent[y][x][1]][parent[y][x][0]] :
    parent[y][x] = (x,y)
    return x, y
    
  px, py = find(parent[y][x][0], parent[y][x][1])
  parent[y][x] = (px, py)
  return px, py

cnt = 0
for i in range(n):
  for j in range(m):
    if not v[i][j] :
      print('check')
      find(j,i)
      cnt += 1
print(cnt)
  

