###
# 2357. 최솟값과 최댓값
# problem : https://www.acmicpc.net/problem/2357
# status : solved
###

import sys
input = sys.stdin.readline

maxval = 1000000000
min_tree = [0]*int(1e7)
max_tree = [0]*int(1e7)

def init(n, s, e):
  if s == e:
    min_tree[n] = lst[s]
    max_tree[n] = lst[s]
  else :
    m = (s+e)//2
    mina, maxa = init(n*2,s,m)
    minb, maxb = init(n*2+1,m+1,e)
    min_tree[n] = min(mina, minb)
    max_tree[n] = max(maxa, maxb)
  return min_tree[n], max_tree[n]
  
def find(n, s, e, l, r):
  if r < s or l > e :
    return maxval+1, 0
  if l <= s and e <= r :
    return min_tree[n], max_tree[n]
  m = (s+e)//2
  mina, maxa = find(n*2, s, m, l, r)
  minb, maxb = find(n*2+1, m+1, e, l, r)
  return min(mina,minb), max(maxa,maxb)

N,M = map(int, input().split())
lst = [int(input()) for _ in range(N)]
init(1,0,N-1)
for a, b in [list(map(int, input().split())) for _ in range(M)]:
  print(*find(1,0,N-1,a-1,b-1))
