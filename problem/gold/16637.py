###
# 16637. 괄호 추가하기
# problem : https://www.acmicpc.net/problem/16637
# status : solved
###

import re

N = int(input())
num_len = N//2+1
expression = input().strip()
ops = re.findall('[^0-9]', expression)
nums = re.findall('[0-9]', expression)
visited = [False]*num_len
answer = -float('inf')

cal = lambda x, y, op : eval(str(x)+op+str(y))

def calculate():
  result, cnt = 0, 0
  prev_ops = '+'
  while cnt < num_len :
    if visited[cnt] :
      tmp_result = nums[cnt]
      while True:
        tmp_result = cal(tmp_result, nums[cnt+1], ops[cnt])
        cnt += 1
        if cnt >= num_len-1 or visited[cnt] : break
      result = cal(result, tmp_result, prev_ops)
    else :
      result = cal(result, nums[cnt], prev_ops)
    if cnt < num_len-1 : prev_ops = ops[cnt]
    cnt += 1

  return result
    
def dfs(pnt, bracket):
  global answer
  if pnt == num_len :
    if bracket : return
    result = calculate()
    answer = max(answer, result)
    return

  if not bracket : dfs(pnt+1, bracket)
  visited[pnt] = True
  dfs(pnt+1, not bracket)
  visited[pnt] = False

dfs(0, False)
print(answer)
    
