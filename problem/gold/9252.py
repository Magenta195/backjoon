###
# 9252. LCS 2
# problem : https://www.acmicpc.net/problem/9252
# status : solved
###

l = input().strip()
r = input().strip()

dp = [[0]*(len(l)+1) for _ in range(len(r)+1)]

for i in range(1,len(r)+1):
  for j in range(1,len(l)+1):
    if r[i-1] == l[j-1] :
      dp[i][j] = dp[i-1][j-1] + 1
    else :
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

backtrack = ''
i, j = len(r), len(l)
while dp[i][j] != 0:
  if r[i-1] == l[j-1] :
    backtrack += r[i-1]
    i -= 1
    j -= 1
  else : 
    if dp[i-1][j] > dp[i][j-1] : i -= 1
    else : j -= 1

print(dp[len(r)][len(l)])
if dp[len(r)][len(l)] > 0 : print(backtrack[-1::-1])
