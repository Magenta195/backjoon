###
# 11557. Yangjojang of The Year
# problem : https://www.acmicpc.net/problem/11557
# status : solved
###

for _ in range(int(input())):
  MAX = 0
  M_n = ''
  for _ in range(int(input())):
    name, num = input().split()
    if int(num) > MAX :
      MAX, M_n = int(num), name
  print(M_n)
