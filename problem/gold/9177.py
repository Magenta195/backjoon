###
# 9177. 단어 섞기
# problem : 
# status : solved
# time : 00:14:27
###

import sys
input = sys.stdin.readline

for i in range(int(input())):
  a, b, c = input().split()
  alen, blen, clen = len(a), len(b), len(c)
  
  dp = [[-1]*(blen+1) for _ in range(alen+1)]
  def dfs(aidx, bidx, cidx):
    if cidx == clen :
      return 1
    if dp[aidx][bidx] > -1 :
      return dp[aidx][bidx]
      
    judge = 0
    if aidx < alen and a[aidx] == c[cidx] :
      judge += dfs(aidx+1, bidx, cidx+1)
    if bidx < blen and b[bidx] == c[cidx] :
      judge += dfs(aidx, bidx+1, cidx+1)
    dp[aidx][bidx] = judge
    return judge

  judge = 'yes' if dfs(0,0,0) > 0 else 'no'
  print('Data set {:d}: {:s}'.format(i+1, judge))
