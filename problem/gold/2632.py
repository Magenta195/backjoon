###
# 2632. 피자 판매
# problem : 00:34:51
# status : solved
# time : https://www.acmicpc.net/problem/2632
###

import sys
from collections import defaultdict
input = sys.stdin.readline

pizza_size = int(input())
m, n = map(int, input().split())
m_lst = [int(input()) for _ in range(m)]
n_lst = [int(input()) for _ in range(n)]

def get_pizza_dict(size, pizza_lst, pizza_dict) :
  for i in range(size) :
    sum_result = pizza_lst[i]
    pizza_dict[sum_result] += 1
    for j in range(1, size-1) :
      sum_result += pizza_lst[(i+j)%size]
      pizza_dict[sum_result] += 1
      
  pizza_dict[sum(pizza_lst)] += 1
  pizza_dict[0] += 1
        
m_sum_dict = defaultdict(int)
n_sum_dict = defaultdict(int)
get_pizza_dict(m, m_lst, m_sum_dict)
get_pizza_dict(n, n_lst, n_sum_dict)

ans = 0 
for key, val in m_sum_dict.items() :
  ans += val*n_sum_dict[pizza_size - key]

print(ans)
