###
# 2473. 세 용액
# problem ; https://www.acmicpc.net/problem/2473
# status : solved
###

n = int(input())

def check(l_lst, r_lst):
  best = 3 * 1e11
  
  for k in r_lst :
    i, j = 0, len(l_lst)-1
    while i < j :
      s = l_lst[i] + l_lst[j] + k
      if s == 0:
        return (l_lst[i], l_lst[j], k)
      else :
        if abs(best) > abs(s) :
          cnt = (l_lst[i], l_lst[j], k)
          best = s
        if s < 0 :
          i += 1
        else :
          j -= 1
  
  for k in l_lst :
    i, j = 0, len(r_lst)-1
    while i < j:
      s = r_lst[i] + r_lst[j] + k
      if s == 0:
        return (k, r_lst[i], r_lst[j])
      else :
        if abs(best) > abs(s) :
          cnt = (k, r_lst[i], r_lst[j])
          best = s
        if s < 0 :
          i += 1
        else :
          j -= 1
          
  return cnt

lst = sorted(list(map(int, input().split())))
for m in range(n-1):
  if lst[m] >= 0 : break

if m == 0 :
  print(lst[0], lst[1], lst[2])
elif m == n-1:
  print(lst[-3], lst[-2], lst[-1])
else :
  l_lst = lst[:m]
  r_lst = lst[m:]
  l, c, r = check(l_lst, r_lst)
  if len(l_lst) > 3 and abs(l_lst[-3]+l_lst[-2]+l_lst[-1]) < abs(l+c+r) :
    l, c, r = l_lst[-3], l_lst[-2], l_lst[-1]
  if len(r_lst) > 3 and abs(r_lst[0]+r_lst[1]+r_lst[2]) < abs(l+c+r):
    l, c, r = r_lst[0], r_lst[1], r_lst[2]

  print(l, c, r)
