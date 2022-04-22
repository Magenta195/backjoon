###
# 2749. 피보나치 수 3
# problem : https://www.acmicpc.net/problem/2749
# status : solved
###

n = int(input())
n %= 15*(10**5)
a, b = 0, 1
for _ in range(n) : 
  a, b = (a+b) % (10**6), a
print(a)
