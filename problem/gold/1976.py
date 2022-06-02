###
# 1976. 여행 가자
# problem : https://www.acmicpc.net/problem/1976
# status : solved
# time : ???
###

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
MAX = float('inf')
adj = [list(map(int,input().split())) for _ in range(N)]
parent = list(range(N))

def find(A):
  if parent[A] == A:
    return A
  
  parent[A] = find(parent[A])
  return parent[A]

def union(A,B):
  pA = find(A)
  pB = find(B)
  if pA > pB :
    parent[pA] = pB
  else : 
    parent[pB] = pA

for i in range(N) :
 for j in range(N):
   if i != j and adj[i][j] == 1 :
     union(i,j)

lst = list(map(int,input().split()))
for i in range(M-1):
  if parent[lst[i]-1] != parent[lst[i+1]-1]:
    print("NO")
    exit()
print("YES")
  
