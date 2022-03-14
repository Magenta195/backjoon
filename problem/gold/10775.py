###
# 10775. 공항
# problem : https://www.acmicpc.net/problem/10775
# status : solved
###

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

g = int(input())
gate = list(range(g+1))
p = int(input())

def find(a) :
  if gate[a] == a:
    return a
  p = find(gate[a])
  gate[a] = p
  return p

def union(da, db):
  if da < db :
    gate[db] = da
  else :
    gate[da] = db

cnt = 0
for i in range(p):
  n = int(input())
  dn = find(n)
  if dn == 0: break
  cnt += 1
  union(dn, dn-1)
  
print(cnt)
