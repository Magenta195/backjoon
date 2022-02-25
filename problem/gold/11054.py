###
# 11054. 가장 긴 바이토닉 부분 수열
# problem : https://www.acmicpc.net/problem/11054
# status : solved
###
n = int(input())
lst = list(map(int, input().split()))
c_order = [0]*n
d_order = [0]*n

for i in range(n):
  for j in range(i):
    if lst[i] > lst[j]:
      c_order[i] = max(c_order[i], c_order[j])
    if lst[n-i-1] > lst[n-j-1]:
      d_order[n-i-1] = max(d_order[n-i-1], d_order[n-j-1])
  c_order[i] += 1
  d_order[n-i-1] += 1

print(max([x+y-1 for x, y in zip(c_order, d_order)]))
