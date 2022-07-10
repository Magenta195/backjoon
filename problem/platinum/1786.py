###
# 1786. 찾기
# problem : https://www.acmicpc.net/problem/1786
# status : solved
# time : 00:??:??
###

T = input().rstrip()
P = input().rstrip()

pi = [0]*len(P)
i = 0
for j in range(1, len(P)):
  while i > 0 and P[i] != P[j] :
    i = pi[i-1]

  if P[i] == P[j] :
    i += 1
    pi[j] = i

i = 0
ans = []
for j in range(len(T)) :
  while i > 0 and P[i] != T[j] :
    i = pi[i-1]

  if P[i] == T[j] :
    i += 1
    if i == len(P) :
      ans.append(j-i+2)
      i = pi[i-1]

print(len(ans))
if ans : print(*ans)
