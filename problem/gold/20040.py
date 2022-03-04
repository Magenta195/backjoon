###
# 20040. 사이클 게임
# problem : https://www.acmicpc.net/problem/20040
# status : solved
###
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

parent = list(range(n))

def find(a):
  if parent[a] == a :
    return a
  p = find(parent[a])
  parent(a) = p
  return p

def union(da, db)
  if da > db :
    parent[da] = db
  else : 
    parent[db] = da

flg = True
for i in range(1, n+1):
  a, b = map(int, input().split())
  da, db = find(a), find(b)
  if da == db :
    flg = False
    break
  else :
    union(da, db)
print(i if not flg else 0)
