###
# 14428. 수열과 쿼리 16
# problem : https://www.acmicpc.net/problem/14428
# status : solved
###

tree = [0]*int(1e7)
import sys
input = sys.stdin.readline

def init(n, s, e):
  if s==e:
    tree[n] = s
  else :
    m = (s+e)//2
    a = init(n*2, s, m)
    b = init(n*2+1, m+1, e)
    tree[n] = a if lst[a] <= lst[b] else b
  return tree[n]

def update(n, s, e, idx):
  if s==e==idx or e < idx or s > idx:
    return
  m = (s+e)//2
  update(n*2, s, m, idx)
  update(n*2+1, m+1, e, idx)
  tree[n] = tree[n*2] if lst[tree[n*2]] <= lst[tree[n*2+1]] else tree[n*2+1]

def minval(n, s, e, l, r):
  if r < s or e < l :
    return 0
  if l <= s and e <= r :
    return tree[n]
  m = (s+e)//2
  a = minval(n*2, s, m, l, r)
  b = minval(n*2+1, m+1, e, l, r)
  return a if lst[a] <= lst[b] else b

N = int(input())
lst = [int(1e9)+1] + list(map(int,input().split()))
init(1,1,N)

M = int(input())
for _ in range(M):
  a, b, c = map(int,input().split())
  if a == 1 :
    lst[b] = c
    update(1,1,N,b)
  else :
    print(minval(1,1,N,b,c))
