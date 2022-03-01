###
# 1509. 펠린드롬 분함
# problem : https://www.acmicpc.net/problem/1509
# status : solved
###
import sys
sys.setrecursionlimit(3000)

lst = input().strip()
n = len(lst)
dp = [1e10]*n
pal_dp = [[0]*n for _ in range(n)]
 
# 주의! pal_dp check를 함수를 통해 재귀적으로 계산하면 타임 오버 가능!
for i in range(n):
  pal_dp[i][i] = True
  if i < n-1:
    pal_dp[i][i+1] = lst[i] == lst[i+1]

for i in range(2, n):
  for j in range(n-i):
    pal_dp[j][j+i] = (lst[j] == lst[j+i]) and pal_dp[j+1][j+i-1]
  
def pal(start):
  if start == n : return 0
  if dp[start] < 1e10 : return dp[start]
  
  for i in range(start, n):
    if pal_dp[start][i]:
      dp[start] = min(1+pal(i+1), dp[start])
  return dp[start]

print(pal(0))
