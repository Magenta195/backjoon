###
# 13172. sigma
# problem : https://www.acmicpc.net/problem/13172
# status : solved
###
n = 1000000007
s = 0
def power(b, t):
  if t == 1 :
    return b % n
  
  p_b = power(b, t//2) % n
  if t % 2 == 1:
    return ((p_b * p_b) % n * (b % n)) % n
  else :
    return (p_b * p_b) % n
  
def euclidean(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
            
for _ in range(int(input())):
  b, a = map(int, input().split())
  r = euclidean(a, b)
  a_, b_ = a // r, b //r
  b__ = power(b_, n-2)
  s += (a_ * b__) % n
  s %= n
print(s % n)
