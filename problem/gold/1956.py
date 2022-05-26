###
# 1956. 운동
# problem : https://www.acmicpc.net/problem/1956
# status : solved
# time : 00:22:42
###

V,E =map(int,input().split())
MAX = float('inf')
ans = MAX
lst = [[MAX]*V for _ in range(V)]
for _ in range(E):
  a,b,c = map(int,input().split())
  lst[a-1][b-1] = c

for k in range(V):
  for i in range(V):
    for j in range(V):
      if lst[i][j] > lst[i][k] + lst[k][j] :
        lst[i][j] = lst[i][k] + lst[k][j]

for i in range(V-1):
  for j in range(i+1,V):
    if lst[i][j] < MAX and lst[j][i] < MAX :
      ans = min(ans, lst[i][j]+lst[j][i])

print(ans if ans < MAX else -1)
