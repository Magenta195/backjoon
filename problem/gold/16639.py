###
# 16639. 괄호 추가하기 3
# problem : https://www.acmicpc.net/problem/16639
# status : solved
###

N = int(input())
lst = list(input())
MAX = float('inf')
if N == 1 :
  print(lst[0])
  exit()
def cal(a,b,expr) :
  if expr == '+' :
    return a+b
  elif expr == '-' :
    return a-b
  return a*b
  
def full_cal(a,b,expr) :
  m, n = MAX, -MAX
  for i in range(2):
    for j in range(2):
      r = cal(a[i],b[j],expr)
      m,n = min(m,r), max(n,r)
  return m,n
  
e_lst, n_lst = [],[]
for i in lst :
  if i in ['+','-','*'] :
    e_lst.append(i)
  else :
    n_lst.append(int(i))

dp = [[[MAX, -MAX] for _ in range(N//2+1)] for _ in range(N//2+1)]
for i in range(N//2+1) :
  dp[i][i][0], dp[i][i][1] = n_lst[i], n_lst[i]
  if i < N//2 :
    dp[i][i+1][0] = cal(n_lst[i],n_lst[i+1],e_lst[i])
    dp[i][i+1][1] = cal(n_lst[i],n_lst[i+1],e_lst[i])

for i in range(2, N//2+1):
  for j in range(N//2+1-i):
    for k in range(i):
      m, n = full_cal(dp[j][j+k], dp[j+k+1][j+i], e_lst[j+k])
      dp[j][j+i][0], dp[j][j+i][1] = min(dp[j][j+i][0], m), max(dp[j][j+i][1], n)

print(dp[0][-1][1])
