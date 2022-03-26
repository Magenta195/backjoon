###
# 3830. 교수님은 기다리지 않는다
# problem : https://www.acmicpc.net/problem/3830
# status : solved
###
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def find(x):
    if x == parent[x]:
        return x
    else:
        r = find(parent[x])
        dist[x] += dist[parent[x]]
        parent[x] = r
        return parent[x]
def union(x, y, k):
    xroot = parent[x]
    yroot = parent[y]
    if xroot != yroot:
        parent[yroot] = xroot
        dist[yroot] = (dist[x] + k) - dist[y]
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    parent = [i for i in range(n + 1)]
    dist = [0 for i in range(n + 1)]
    for i in range(m):
        a = list(map(str, input().split()))
        find(int(a[1]))
        find(int(a[2]))
        if a[0] == "!":
            union(int(a[1]), int(a[2]), int(a[3]))
        else:
            if parent[int(a[1])] == parent[int(a[2])]:
                print(dist[int(a[2])] - dist[int(a[1])])
            else:
                print("UNKNOWN")
      
    
