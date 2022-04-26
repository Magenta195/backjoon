###
# 1026. 보물
# problem : https://www.acmicpc.net/problem/1026
# status : solved
###

N = int(input())
a_lst = sorted(list(map(int,input().split())))
b_lst = sorted(list(map(int,input().split())), reverse=True))
print(sum([x+y for x, y in zip(a_lst, b_lst)]))
