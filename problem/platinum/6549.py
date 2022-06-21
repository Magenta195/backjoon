###
# 6549. 히스토그램에서 가장 큰 직사각형
# problem : https://www.acmicpc.net/problem/6549
# status : solved
# time : 01:02:54
###

# trial 1(segment tree)
import sys
sys.setrecursionlimit(10**8)

while True:
  n, *lst = map(int, input().split())
  if n == 0 : break

  tree = [0]*(2**18)
  mh = max(lst)
  
  def init(l, r, node):
    if l == r :
      tree[node] = l
      return
    m = (l + r) // 2
    init(l, m, node*2)
    init(m+1, r, node*2+1)
    tree[node] = tree[node*2] if lst[tree[node*2]] <= lst[tree[node*2+1]] else tree[node*2+1]

  def query(l, r, s, e, node):
    if e < l or s > r :
      return -1
    if s <= l and r <= e :
      return tree[node]

    m = (l+r) // 2
    v1 = query(l, m, s, e, node*2)
    v2 = query(m+1, r, s, e, node*2+1)
    if v1 == -1 : return v2
    if v2 == -1 : return v1
    return v1 if lst[v1] <= lst[v2] else v2

  def mul(l, r):
    if l == r : return lst[r]
    if r < l : return 0
    
    m_node = query(0, n-1, l, r, 1)
    v1 = (r-l+1)*lst[m_node]
    
    v2 = mul(l, m_node-1)
    v3 = mul(m_node+1, r)

    return max(v1, v2, v3)

  init(0, n-1, 1)
  print(mul(0,n-1))
  
# trial 2 (stack)

from collections import deque

while True:
  n, *lst = map(int, input().split())
  if n == 0 : break

  ans = 0
  stk = deque([])
  for i in range(n):
    if not stk :
      stk.append((lst[i],i))
      continue
    h, j = stk[-1]
    if h < lst[i] :
      stk.append((lst[i],i))
    elif h > lst[i] :
      while stk and stk[-1][0] > lst[i]:
        h, j = stk.pop()
        ans = max(ans, h*(i-j))
      stk.append((lst[i],j))

  while stk:
    h, j = stk.pop()
    ans = max(ans, h*(n-j))
  print(ans)
