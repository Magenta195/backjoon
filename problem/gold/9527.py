###
# 9527. 1의 개수 세기
# problem : https://www.acmicpc.net/problem/9527
# status : 
###

a, b = map(int, input().split())

def cnt(x):
  c, k = 0, 0
  while 2**k <= x:
    p = 2**(k+1)
    p_cnt = (x+1)//p
    c += p_cnt * (p // 2)
    
    left = (x+1) % p
    c += max(0, left - (p//2))
    k += 1
  return c

print(cnt(b) - cnt(a-1))
