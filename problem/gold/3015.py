###
# 3015. 오아시스 재결합
# problem : https://www.acmicpc.net/problem/3015
# status : solved
###

import sys
input = sys.stdin.readline
stk = []
ans = 0
for _ in range(int(input())):
  h = int(input())
  
  while stk and stk[-1][0] < h :
    ans += stk.pop()[1]
   
  if not stk :
    stk.append((h,1))  
  elif stk[-1][0] == h :
    cnt = stk.pop()[1]
    ans += cnt
    if stk : ans += 1    
    stk.append((h,cnt+1))
  else : 
    stk.append((h,1))
    ans += 1

print(ans)
