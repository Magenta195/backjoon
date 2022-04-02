###
# 2243.사탕상자
# problem : https://www.acmicpc.net/problem/2243
# status : solved
###

import sys
input = sys.stdin.readline

n = int(input())

MAX = 1000000
tree = [0]*(MAX*4 + 1)

def update(n, s, e, p, v):
  if s == e == p :
    tree[n] += v
    return
  if e < p or p < s :
    return
  m = (s + e) // 2
  update(n*2, s, m, p, v)
  update(n*2+1, m+1, e, p, v)
  tree[n] = tree[n*2] + tree[n*2+1]
  
def find(n, s, e, p):
  if s == e :
    tree[n] -= 1
    return s
  
  m = (s + e) // 2
  a = find(n*2, s, m, p) if tree[n*2] >= p else find(n*2+1, m+1, e, p-tree[n*2])
  tree[n] = tree[n*2] + tree[n*2+1]
  return a
  
for _ in range(n):
  a, *b = map(int,input().split())
  if a == 1 :
    print(find(1, 1, MAX, b[0]))
  else :
    update(1, 1, MAX, b[0], b[1])
  
