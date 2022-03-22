###
# 11505. 구간 곱 구하기
# problem : https://www.acmicpc.net/problem/11505
# status : solved
###

import sys
input = sys.stdin.readline
num = 1000000007

def init(node, start, end):
  if start == end :
    tree[node] = lst[start]
  else :
    mid = (start + end)//2
    tree[node] = (init(node*2, start, mid) * init(node*2 + 1, mid+1, end)) % num
  return tree[node]

def mul(node, start, end, l, r):
  if l > end or r < start :
    return 1
  if l <= start and r >= end :
    return tree[node]
  mid = (start + end)//2
  return (mul(node*2, start, mid, l, r)*mul(node*2+1, mid+1, end, l, r)) % num

def update(node, start, end, index, value):
  if index < start or index > end : return 1
  if start == end == index :
    tree[node] = value
    return tree[node]
  if start != end :
    mid = (start + end)//2
    update(node*2, start, mid, index, value)
    update(node*2+1, mid+1, end, index, value)
    tree[node] = (tree[node*2]*tree[node*2+1])%num

n,m,k = map(int, input().split())
tree = [0]*int(1e7)
lst = [int(input()) for _ in range(n)]
init(1,0,n-1)
for a, b, c in [list(map(int,input().split())) for _ in range(m+k)]:
  if a == 1:
    lst[b-1] = c
    update(1,0,n-1,b-1,c)
  else:
    print(int(mul(1,0,n-1,b-1,c-1)))
    
### segment tree를 이용한 비슷한 방식으로 다음 문제가 더 존재한다.
###
# 2042. 구간 합 구하기
# problem : https://www.acmicpc.net/problem/2042
# status : solved
###
import sys
input = sys.stdin.readline

def init(node, start, end):
  if start == end :
    tree[node] = lst[start]
  else :
    mid = (start + end)//2
    tree[node] = init(node*2, start, mid) + init(node*2 + 1, mid+1, end)
  return tree[node]

def _sum(node, start, end, l, r):
  if l > end or r < start :
    return 0
  if l <= start and r >= end :
    return tree[node]
  mid = (start + end)//2
  return _sum(node*2, start, mid, l, r) + _sum(node*2+1, mid+1, end, l, r)

def update(node, start, end, index, value):
  if index < start or index > end : return 0
  if start == end == index :
    tree[node] = value
    return tree[node]
  if start != end :
    mid = (start + end)//2
    update(node*2, start, mid, index, value)
    update(node*2+1, mid+1, end, index, value)
    tree[node] = tree[node*2] + tree[node*2+1]

n,m,k = map(int, input().split())
tree = [0]*int(1e7)
lst = [int(input()) for _ in range(n)]
init(1,0,n-1)
for a, b, c in [list(map(int,input().split())) for _ in range(m+k)]:
  if a == 1:
    lst[b-1] = c
    update(1,0,n-1,b-1,c)
  else:
    print(int(_sum(1,0,n-1,b-1,c-1)))
