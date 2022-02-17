###
# 11727. 2xn 타일링 2
# problem : https://www.acmicpc.net/problem/11727
# status : solved
###

n = int(input())
p = [0]*n

for i in range(n):
  if i == 0:
    p[i] = 1
  elif i == 1:
    p[i] = 3 # 2 x 2, 1 x 2 x 2, 2 x 1 x 2
  else :
    p[i] = p[i-1] + p[i-2] * 2 
print(p[-1] % 10007)
