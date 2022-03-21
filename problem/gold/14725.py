###
# 14725. 개미굴
# problem : https://www.acmicpc.net/problem/14725
# status : solved
###

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

tree = {}
N = int(input())
for _ in range(N):
  n, *n_lst = input().strip().split()
  dic = tree
  for i in n_lst :
    if i not in dic:
      dic[i] = {}
    dic = dic[i]

def search(dic, depth):
  for i in sorted(dic.keys()):
    print('--'*depth + i)
    if dic[i] :
      search(dic[i], depth+1)

search(tree,0)
