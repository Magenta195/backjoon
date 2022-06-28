###
# 14002. 가장 큰 증가하는 부분 수열 2
# problem : https://www.acmicpc.net/problem/14002
# status : solved
# time : 00:26:58
###

### LCS 
N = int(input())
lst = list(map(int, input().split()))

stk = []
rcd = []

for i in lst :
  if not stk or stk[-1] < i :
    rcd.append((len(stk), i))
    stk.append(i)
    continue
  s, e = 0, len(stk)-1
  while s < e :
    m = (s+e) // 2
    if i > stk[m] :
      s = m+1
    else :
      e = m
  stk[e] = i
  rcd.append((e, i))

print(len(stk))
k = len(stk)-1
rd = []
for i, n in reversed(rcd):
  if i == k :
    k -= 1
    rd.append(n)
  if k < 0 : break

print(*reversed(rd))

### DP
N = int(input())
lst = list(map(int, input().split()))

dp = [[lst[i]] for i in range(N)]

for i in range(1,N):
  for j in range(i):
    if lst[j] < lst[i] and len(dp[i]) < len(dp[j]) + 1 :
      dp[i] = dp[j].copy() + [lst[i]]
max_lst = max(dp, key = lambda x:len(x))
print(len(max_lst))
print(*max_lst)
