###
# 1176. 섞기
# problem : https://www.acmicpc.net/problem/1176
# status : solved
###

N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]

dp = [[-1]*N for i in range(1<<N)]

def solution(last, visited):
  if dp[visited][last] > -1:
    return dp[visited][last]
  if visited == (1 << N) - 1 :
    return 1
  
  tmp = 0
  for i in range(N):
    if not (1 << i) & visited and abs(lst[last] - lst[i]) > K:
      tmp += solution(i, visited | (1 << i))
  dp[visited][last] = tmp
  return tmp

ans = 0
for i in range(N):
  ans += solution(i, (1<<i))

print(ans)
      
