###
# 5639.이진 검색 트리
# problem : https://www.acmicpc.net/problem/5639
# status : solved
###
import sys
sys.setrecursionlimit(10100)
l = list(map(int, sys.stdin.readlines()))

def post(lst):
  if len(lst) <= 1 :
    return lst
  
  for i in range(1, len(lst)) :
    if lst[0] > lst[i] : continue
    return post(lst[1:i])+post(lst[i:])+[lst[0]]
  return post(lst[1:]) + [lst[0]]

print(*post(l), sep='\n')
