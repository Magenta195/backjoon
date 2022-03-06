###
# 2623. 음악프로그램
# problem : https://www.acmicpc.net/problem/2623
# status : solved
###

n, m = map(int, input().split())
g = { key : [] for key in range(1, n+1) }
q, ans = [], []
degree = [0]*(n+1)
for _ in range(m):
  t, *t_lst = map(int, input().split())
  for i in range(t):
    if i > 0:
      degree[t_lst[i]] += 1
    if i < t-1 :
      g[t_lst[i]].append(t_lst[i+1])
      
for i in range(1, n+1):
  if degree[i] == 0:
    q.append(i)

while q:
  i = q.pop(0)
  ans.append(i)
  for j in g[i] :
    degree[j] -= 1
    if degree[j] == 0:
      q.append(j)
print(0) if len(ans) < n else print(*ans, sep='\n')
  
