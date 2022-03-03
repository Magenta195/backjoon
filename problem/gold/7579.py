###
# 7579. 앱
# problem : https://www.acmicpc.net/problem/7579
# status : solved
###

### trial 1 (greedy, 틀림)
n, m = map(int, input().split())

m_lst = list(map(int, input().split()))
c_lst = list(map(int, input().split()))

needed = sum(m_lst) - n

lst = sorted([(y,y/x,i) for i,(x,y) in enumerate(zip(m_lst,c_lst))], key = lambda x:(x[0], x[1]))
s, a = 0, 0
while a < m :
  x = lst.pop(0)
  s += c_lst[x[2]]
  a += m_lst[x[2]]
print(s)

### trial 2 (DP)
n, m = map(int, input().split())

m_lst = list(map(int, input().split()))
c_lst = list(map(int, input().split()))

dp = [[0]*(n+1) for _ in range(sum(c_lst)+1)]

for i in range(sum(c_lst)+1):
  for j in range(1, n+1):
    b = m_lst[j-1]
    c = c_lst[j-1]
    if i < c :
      dp[i][j] = dp[i][j-1]
    else :
      dp[i][j] = max(dp[i][j-1], dp[i-c][j-1] + b)
  if max(dp[i]) >= m:
    print(i)
    break
    
    
      
