###
# 17840. 피보나치 음악
# problem : https://www.acmicpc.net/problem/17840
# status : solved
###

import sys
input = sys.stdin.readline

Q, M = map(int, input().split())
dp = [[-1]*M for _ in range(M)]
dp[0][1] = 0
lst = [1]
pre, now, cnt = 1, 1, 1

while (pre, now) != (0,1) :
  dp[pre][now] = cnt
  tmp = list(map(int, str(now)))
  lst += tmp
  cnt += len(tmp)
  pre, now = now, (pre+now) % M
for _ in range(Q):
  num = int(input())
  print(lst[num-1] if num < cnt else lst[num % cnt - 1])
