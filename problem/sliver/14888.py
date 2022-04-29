###
# 14888. 연산자 끼워넣기
# problem : https://www.acmicpc.net/problem/14888
# status : solved
###

N = int(input())
A = list(map(int,input().split()))
op_lst = list(map(int, input().split()))
INF = 10**9
MIN, MAX = INF, -INF
def ops(i, a, b):
  if i == 0: return a+b
  elif i == 1: return a-b
  elif i == 2: return a*b
  else : 
    return a//b if a > 0 else -((-a)//b)

def dfs(cnt, val):
  global MIN, MAX
  if cnt == N-1 :
    MIN = min(MIN, val)
    MAX = max(MAX, val)
    return
  for i in range(4):
    if op_lst[i] > 0 :
      op_lst[i] -= 1
      dfs(cnt+1, ops(i, val, A[cnt+1]))
      op_lst[i] += 1
dfs(0, A[0])
print(MAX, MIN, sep='\n')
