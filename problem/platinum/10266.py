###
# 10266. 시계 사진들
# problem : https://www.acmicpc.net/problem/10266
# status : solved
# time : 00:17:45
###

N = int(input())
lst1 = sorted(list(map(int, input().split())))
lst2 = sorted(list(map(int, input().split())))

gap1 = [(lst1[(i+1)%N] - lst1[i])%360000 for i in range(N)]
gap2 = [(lst2[(i+1)%N] - lst2[i])%360000 for i in range(N)]
gap1 += gap1
pi = [0]*N
i = 0
for j in range(1, N):
  while i > 0 and gap2[i] != gap2[j] :
    i = pi[i-1]

  if gap2[i] == gap2[j] :
    i += 1
    pi[j] = i

i = 0
for j in range(N*2) :
  while i > 0 and gap2[i] != gap1[j] :
    i = pi[i-1]

  if gap2[i] == gap1[j] :
    i += 1
    if i == N :
      print('possible')
      exit()
      
print('impossible')
