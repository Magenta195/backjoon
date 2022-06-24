###
# 4195. 친구 네트워크
# problem : https://www.acmicpc.net/problem/4195
# status : solved
# time : 00:35:45
###

import sys
input = sys.stdin.readline

for _ in range(int(input())):
  parent = dict()
  def find(a):
    if parent[a][0] == a :
      return parent[a]
    parent[a] = find(parent[a][0])
    return parent[a]

  def union(pa, pb, s):
    if pa < pb :
      parent[pb] = parent[pa] = (pa, s)
    else :
      parent[pa] = parent[pb] = (pb, s)

  for i in range(int(input())):
    a, b = input().split()
    flg = True
    if a not in parent :
      parent[a] = (a, 1)
    if b not in parent :
      parent[b] = (b, 1)

    pa = find(a)
    pb = find(b)

    if pa[0] == pb[0] :
      print(pa[1])
    else :
      union(pa[0],pb[0],pa[1]+pb[1])
      print(pa[1]+pb[1])
