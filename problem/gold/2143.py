###
# 2143. 두 배열의 합
# problem : https://www.acmicpc.net/problem/2143
# status : solved
###
import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
n_lst = list(map(int,input().split()))
n_sum = sum(n_lst)

ln_lst = []
for i in range(n):
  ln_lst.append(n_sum)
  tmp = n_sum
  for j in range(n-1, i, -1):
    tmp -= n_lst[j]
    ln_lst.append(tmp)
  n_sum -= n_lst[i]
  
m = int(input())
m_lst = list(map(int,input().split()))
m_sum = sum(m_lst)

lm_lst = []
for i in range(m):
  lm_lst.append(m_sum)
  tmp = m_sum
  for j in range(m-1, i, -1):
    tmp -= m_lst[j]
    lm_lst.append(tmp)
  m_sum -= m_lst[i]
  
ln_lst.sort()
lm_lst.sort(reverse=True)
cnt = 0
i, j = 0, 0
while i < len(ln_lst) and j < len(lm_lst):
  if ln_lst[i] + lm_lst[j] == t :
    ci, cj = 1, 1
    ti, tj = ln_lst[i], lm_lst[j]
    i += 1
    j += 1
    while i < len(ln_lst) and ln_lst[i] == ti:
      i += 1
      ci += 1
    while j < len(lm_lst) and lm_lst[j] == tj:
      j += 1
      cj += 1
    cnt += ci * cj
  elif ln_lst[i] + lm_lst[j] > t : j += 1
  else : i += 1

print(cnt)
