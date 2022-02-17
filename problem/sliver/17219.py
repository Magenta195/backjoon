
###
# 17219. 비밀번호 찾기
# problem : https://www.acmicpc.net/problem/17219
# status : solved
###

import sys

n, m = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(n):
  site, pw = sys.stdin.readline().split()
  dic[site] = pw
for _ in range(m):
  print(dic[sys.stdin.readline().strip()])
