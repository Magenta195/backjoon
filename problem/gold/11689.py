###
# 11689. GCD(n,k) = 1
# problem : https://www.acmicpc.net/problem/11689
# status : solved
###

import math
n = int(input())
lst = set()
ans = n
while n >= 2:
  flg = False
  for i in range(2,math.ceil(n**(1/2))+1):
    if n % i == 0:
      lst.add(i)
      n = n // i
      flg = True
      break
  if not flg :
    lst.add(n)
    break

for i in lst :
  ans = int(ans*(1-1/i))
print(ans)
