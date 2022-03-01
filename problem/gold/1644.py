###
# 1644. 소수의 연속합
# problem : https://www.acmicpc.net/problem/1644
# status : solved
###

n = int(input())
if n == 1 : 
  print(0)
  exit()
  
p_num = list(range(n+1))

for i in range(n+1):
  if i < 2 : p_num[i] = 0
  if i ** 2 > n : break
  if p_num[i] == 0 : continue
  j = 2*i
  while j < n+1 :
    p_num[j] = 0
    j += i

p_lst = []
for i in p_num:
  if i == 0: continue
  p_lst.append(i)

i, j, cnt = 0, 1, 0
s = p_lst[0]
while i < j < len(p_lst) + 1 :
  if s < n :
    if j < len(p_lst):
      s += p_lst[j]
    j += 1
  elif s > n :
    s -= p_lst[i]
    i += 1
  else :
    cnt += 1
    if j <  len(p_lst):
      s = s - p_lst[i] + p_lst[j]
    i += 1
    j += 1
    
print(cnt)
    
