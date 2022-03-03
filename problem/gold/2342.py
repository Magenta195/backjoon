###
# 2342. Dance Dance Revolution
# problem : https://www.acmicpc.net/problem/2342
# status :
###

lst = list(map(int,input().split()))

def move(a, b):
  if a == 0:
    return 2 if b > 0 else 0
  if a == b : 
    return 1
  if abs(a-b) % 2 == 1:
    return 3
  return 4

dp = [[[1e10]*5 for _ in range(5)] for i in range(len(lst))]
dp[-1][0][0] = 0
for i in range(len(lst)) :
  if i == len(lst)-1 : break
  for j in range(5):
    for k in range(5):
      dp[i][lst[i]][j] = min(dp[i][lst[i]][j], dp[i-1][k][j] + move(k, lst[i]))
      dp[i][j][lst[i]] = dp[i][lst[i]][j]
      
print(min(map(min, dp[-2]))))
