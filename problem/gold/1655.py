###
# 1655. 가운데를 말해요
# problem : https://www.acmicpc.net/problem/1655
# status : solved
###

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())

minq, maxq = [], []
min_l, max_l = 0, 0

for i in range(N):
  num = int(input())
  if min_l == max_l :
    heappush(maxq, -num)
    max_l += 1
  else : 
    heappush(minq, num)
    min_l += 1

  if minq and minq[0] < -maxq[0]:
    tmp = -heappop(maxq)
    heappush(maxq, -heappop(minq))
    heappush(minq, tmp)
  print(-maxq[0])
