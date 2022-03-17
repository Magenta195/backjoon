###
# 2162. 선분 그룹
# problem : https://www.acmicpc.net/problem/2162
# status : solved(only pypy3)
###
import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
parent = list(range(N))
cnt = [1]*N

def find(a):
  if parent[a] == a :
    return a
  parent[a] = find(parent[a])
  return parent[a]

def union(da, db):
  if da == db : return
  elif da < db :
    parent[db] = da
    cnt[da] += cnt[db]
  else : 
    parent[da] = db
    cnt[db] += cnt[da]

def ccw(ax, bx, cx, ay, by, cy):
  return (ax*by+bx*cy+cx*ay) - (bx*ay+cx*by+ax*cy)

def check(x1, y1, x2, y2, x3, y3, x4, y4):
  c1 = ccw(x1, x2, x3, y1, y2, y3)
  c2 = ccw(x1, x2, x4, y1, y2, y4)
  c3 = ccw(x3, x4, x1, y3, y4, y1)
  c4 = ccw(x3, x4, x2, y3, y4, y2)
  
  if c1*c2 == 0 and c3*c4 == 0:
    return True if (max(x1, x2) >= min(x3, x4) and
      max(y1, y2) >= min(y3, y4) and
      max(y3, y4) >= min(y1, y2) and
      max(x3, x4) >= min(x1, x2)) else False
  else :
    return True if c1*c2 <= 0 and c3*c4 <= 0 else False
  
for i in range(N-1):
  for j in range(i+1, N):
    if check(*lst[i], *lst[j]) :
      di = find(i)
      dj = find(j)
      union(di, dj)
      
ans = 0
for i in range(N):
  if parent[i] == i: ans+=1
print(ans)
print(max(cnt))
