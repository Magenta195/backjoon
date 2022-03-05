###
# 2467. 용액
# problem ; https://www.acmicpc.net/problem/2467
# status : solved
###

n = int(input())

def check(l_lst, r_lst):
  i, j = 0, len(r_lst)-1
  cnt = (i,j)
  best = 2 * 1e11
  while i < len(l_lst) and j > -1 :
    s = l_lst[i] + r_lst[j]
    if s == 0:
      cnt = (i,j)
      break
    else :
      if abs(best) > abs(s) :
        cnt = (i, j)
        best = s
      if s < 0 :
        i += 1
      else :
        j -= 1
  return cnt

lst = list(map(int, input().split()))
for m in range(n-1):
  if lst[m] >= 0 : break

if m == 0 :
  print(lst[0], lst[1])
elif m == n-1:
  print(lst[-2], lst[-1])
else :
  l_lst = lst[:m]
  r_lst = lst[m:]
  cnt = check(l_lst, r_lst)
  l, r = l_lst[cnt[0]], r_lst[cnt[1]]
  if abs(l_lst[-2]+l_lst[-1]) < abs(l+r) :
    l, r = l_lst[-2], l_lst[-1]
  if abs(r_lst[0]+r_lst[-1]) < abs(l+r):
    l, r = r_lst[0], r_lst[-1]

  print(l, r)

    
