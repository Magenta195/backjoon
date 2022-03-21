###
# 15824. 너 봄에는 캡사이신이 맛있단다
# problem : https://www.acmicpc.net/problem/15824
# status : solved
###

n = int(input())
lst = sorted(list(map(int,input().split())))
num = 1000000007
ans = 0
d = [-1]*n

def pow(n):
  if n <= 1:
    return n+1

  if d[n] != -1 : return d[n]
    
  p = pow(n//2) % num
  p = p*p % num

  d[n] = p if n % 2 == 0 else (p * 2) % num
  return d[n]
    
for i in range(n):
  ans += lst[i] * (pow(i) - pow(n-i-1))
  ans %= num
print(ans % num)
