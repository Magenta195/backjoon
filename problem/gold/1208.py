###
# 1202. 보석 도둑
# problem : https://www.acmicpc.net/problem/1202
# status :
###
import sys
from itertools import combinations
input = sys.stdin.readline
n, s = map(int, input().split())
lst = list(map(int, input().split()))
m = n//2

r_lst, l_lst = [], []
for i in range(m):
  for j in combinations(lst[:m], i):
    l_lst.append(sum(j))
for i in range(n-m):
  for j in combinations(lst[m:], i):
    r_lst.append(sum(j))

l_lst.sort()
r_lst.sort(reverse=True)
l_p, r_p = 0, 0

cnt = 0
while l_p < len(l_lst) and r_p < len(r_lst):
  if l_lst[l_p] + r_lst[r_p] == s :
    c1, c2 = 1, 1
    t_lp, t_rp = l_p, r_p
    l_p += 1
    r_p += 1
    while l_p < len(l_lst) and l_lst[t_lp] == l_lst[l_p] :
      c1 += 1
      l_p += 1
    while r_p < len(r_lst) and r_lst[t_rp] == r_lst[r_p] :
      c2 += 1
      r_p += 1
    cnt += c1*c2
  elif l_lst[l_p] + r_lst[r_p] < s :
    l_p += 1
  else : r_p += 1
print(cnt if s != 0 else cnt-1)
