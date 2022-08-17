###
# 1717. 집합의 표현
# problem : https://www.acmicpc.net/problem/1717
# status : solved
# time : 00:06:39
###

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(range(n+1))

def find(a):
  global parent
  if a == parent[a] :
    return a
  parent[a] = find(parent[a])
  return parent[a]

def union(parent_a, parent_b):
  global parent
  if parent_a > parent_b :
    parent_a, parent_b = parent_b, parent_a
  parent[parent_a] = parent_b

def solution():
  global m
  for _ in range(m):
    order, a, b = map(int, input().split())
    parent_a, parent_b = find(a), find(b)
    if order == 0 :
      union(parent_a, parent_b)
    else :
      print('YES' if parent_a == parent_b else 'NO')

solution()
