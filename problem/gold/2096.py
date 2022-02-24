###
# 2096 내려가기
# problem : https://www.acmicpc.net/problem/2096
# status : solved
###
import sys
input = sys.stdin.readline
n = int(input())

for i in range(n) :
  lst = list(map(int, input().split()))
  if i == 0 :
    _min = lst.copy()
    _max = lst.copy()
  else :
    _min[0], _min[1], _min[2] = min(_min[:2]), min(_min), min(_min[1:])
    _max[0], _max[1], _max[2] = max(_max[:2]), max(_max), max(_max[1:])
    for j in range(3):
      _min[j] += lst[j]
      _max[j] += lst[j]
print(max(_max), min(_min))


