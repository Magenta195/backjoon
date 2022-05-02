###
# 14889. 스타트와 링크
# problem : https://www.acmicpc.net/problem/14889
# status : solved
###

# trial 1 (solved)

import sys
input = sys.stdin.readline

N = int(input())
MAX = 100*N
n_lst = list(range(N))
lst = [list(map(int,input().split())) for _ in range(N)]

def dfs(start, cnt, val_lst):
  if cnt == N // 2 :
    val = 0
    tmp_lst = list(set(n_lst) - set(val_lst))
    
    for i in tmp_lst :
      for j in tmp_lst :
        val -= lst[i][j]
    for i in val_lst :
      for j in val_lst :
        val += lst[i][j]
    
    return abs(val)
  
  if start >= N :
    return MAX
  
  val = MAX
  for i in range(start, N):
    val = min(val, dfs(i+1, cnt+1, val_lst+[i]))
  return val

print(dfs(0,0,[]))

# trial 2 (with combinations, solved)
from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
n_lst = list(range(N))
lst = [list(map(int,input().split())) for _ in range(N)]
val = 100*N

for i_comb in combinations(n_lst, N//2):
  n_comb = list(set(n_lst)-set(i_comb))
  tmp = 0
  for i in i_comb :
    for j in i_comb :
      tmp -= lst[i][j]
  for i in n_comb :
    for j in n_comb :
      tmp += lst[i][j]
  val = min(val, abs(tmp))
print(val)
  
