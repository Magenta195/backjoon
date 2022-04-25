###
# 13458. 시험 감독
# problem : https://www.acmicpc.net/problem/13458
# status : solved
###

from math import ceil

N = int(input())
lst = list(map(int,input().split()))
B, C = map(int, input().split())
print(sum([max(1, ceil((i - B) / C)+1) for i in lst]))
