###
# 4354. 문자열 제곱
# problem : https://www.acmicpc.net/problem/4354
# status : solved
###

while True :
  str = input().strip()
  if str == '.' : break

  pi = [0]*len(str)
  i = 0
  for j in range(1, len(str)):
    while i > 0 and str[i] != str[j] :
      i = pi[i-1]
    if str[i] == str[j] :
      i += 1
      pi[j] = i

  l = len(str) - pi[-1]
  print(1 if len(str) % l != 0 else len(str) // l)
