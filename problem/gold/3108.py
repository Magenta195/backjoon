###
# 3108. 로고
# problem : https://www.acmicpc.net/problem/3108
# status : solved
# time : 00:56:02
###

import sys
input = sys.stdin.readline

N = int(input())
parent = list(range(N+1))
lst = [[0,0,0,0]] + [list(map(int, input().split())) for _ in range(N)]


def overlap(a, b):
  if a[0] > b[0] and a[1] > b[1] and a[2] < b[2] and a[3] < b[3] :
    return False
  if a[0] < b[0] and a[1] < b[1] and a[2] > b[2] and a[3] > b[3] :
    return False
  if b[0] > a[2] or a[0] > b[2] or b[1] > a[3] or a[1] > b[3] :
    return False
  return True
  
                
def find(a):
  if parent[a] == a :
    return a
  parent[a] = find(parent[a])
  return parent[a]

def union(a, b):
  fa = find(a)
  fb = find(b)
  if fa < fb :
    parent[fb] = fa
  else :
    parent[fa] = fb

for i in range(N+1):
  for j in range(N+1):
    if i == j : continue
    if overlap(lst[i], lst[j]):
        union(i, j)
        
for i in range(N+1):
  find(i)
print(len(set(parent))-1)
