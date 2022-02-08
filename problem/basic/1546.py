import sys

n = int(sys.stdin.readline())
lst = [x for x in map(int, sys.stdin.readline().split())]
m = max(lst)
    
print(sum(lst) * 100 / max(lst) / n)
