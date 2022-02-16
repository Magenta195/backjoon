
# Basic problems

따로 분류할 필요 없는 기본 문제를 정리한 페이지입니다.
본 디렉토리에 등재되는 기준은 다음과 같습니다.

* 문제 수준이 지나치게 쉬운 경우.
* 혹은 solved.ac 기준으로 bronze ~ silver rank에 해당하며, 그 중에서도 기본적인 자료구조, 알고리즘 지식만을 요하는 문제
* 풀이에 대한 link및 설명은 따로 본 파일에 게시하지 않습니다.
* 따라서 이러한 문제는 풀이 시 upload 3문제 이상을 원칙으로 합니다.
* 2741번대부터 code는 별도의 파일을 생성하지 않고 본 list에 기술하는 것을 원칙으로 합니다.

---

### 1000. A+B

problem : https://www.acmicpc.net/problem/1000

status : **solved**

note : 

***

### 1001. A-B

problem : https://www.acmicpc.net/problem/1001

status : **solved**

note : 

***

### 1152. 단어의 개수

problem : https://www.acmicpc.net/problem/1152

status : **solved**

note : 

***

### 1157. 단어 공부

problem : https://www.acmicpc.net/problem/1157

status : **solved**

note :

***

### 1546. 평균

problem : https://www.acmicpc.net/problem/1546

status : **solved**

note : 

***

### 2439. 별 찍기 2

problem : https://www.acmicpc.net/problem/2439

status : **solved**

note : 

***

### 2475. 검증수

problem : https://www.acmicpc.net/problem/2475

status : **solved**

note : 

***

### 2577. 숫자의 개수

problem : https://www.acmicpc.net/problem/2577

status : **solved**

note : 

***

### 2741. N 찍기

problem : https://www.acmicpc.net/problem/2741

status : **solved**

code :
```
  n = int(input())
  for i in range(n) :
      print(i+1)
```

note : 

***

### 2908. 상수

problem : https://www.acmicpc.net/problem/2908

status : **solved**

code : 
```
a, b = input().split()
print(a[::-1] if int(a[::-1]) > int(b[::-1]) else b[::-1])
```

note :

***

### 10172. 개

problem : https://www.acmicpc.net/problem/10172

status : **solved**

code : 
```
print('|\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')
```

note : 

***

### 10809. 알파벳 찾기

problem : https://www.acmicpc.net/problem/10809

status : **solved**

code : 
```
s = input()

for i in range(97, 123): ### 97 = 'a', 122 = 'z'
    print(s.find(chr(i)))
```

note :

***

### 10998. A x B

problem : https://www.acmicpc.net/problem/10998

status : **solved**

code : 
```
a, b = map(int, input().split())
print(a*b)
```

note :

***

### 4153. 직각삼각형

problem : https://www.acmicpc.net/problem/4153

status : **solved**

code :

```
import sys

while(True):
    i = sorted([ x for x in map(int, sys.stdin.readline().split())])
    if i[0] == 0 : break
    if i[2] ** 2 == i[1] ** 2 + i[0] ** 2 : print('right')
    else : print('wrong')
```

note :

***

### 10240. ACM 호텔

problem : https://www.acmicpc.net/problem/10250

status : **solved**

code :
```
import sys

m = int(sys.stdin.readline())

for _ in range(m):
    h, w, n = map(int, sys.stdin.readline().split())
    nw = n // h if n % h != 0 else n // h - 1
    nh = n % h if n % h != 0 else h
    print(100 * nh + (nw + 1))

```

note:

***

### 10816. 숫자 카드 2

problem : https://www.acmicpc.net/problem/10816

status : **solved**

code :
```
import sys

def sort_func(lst) : ### quicksort
    if len(lst) <= 1 : return lst

    m = lst[0]
    l_lst = list()
    m_lst = list()
    r_lst = list()
    
    for i in lst :
      if i > m : r_lst.append(i)
      elif i == m : m_lst.append(i)
      else : l_lst.append(i)
    
    return sort_func(l_lst) + m_lst + sort_func(r_lst)

n = int(sys.stdin.readline())
n_card = [x for x in map(int, sys.stdin.readline().split())]
n_card = sort_func(n_card)
n_dic = {}

m = int(sys.stdin.readline())
m_card = [x for x in map(int, sys.stdin.readline().split())]


for i in range(n) :
    n_i = n_card[i]
    if n_i not in n_dic :
        idx = i
        cnt = 0
        while idx < n :
            if n_i != n_card[idx] : break
            idx += 1
            cnt += 1
        n_dic[n_i] = cnt
        
for i in m_card :
    print(n_dic[i] if i in n_dic else 0, end=' ')
```

note :
* 두 가지 풀이법이 있습니다. 하나는 먼저 card를 sort하고, sort한 list를 토대로 그 value를 미리 세어 놓기.
* 그리고 다른 하나는 sort를 진행하지 않고 binary search를 하는 방법입니다.
* 다만 2 방법 모두 n_card에 대한 unique value를 먼저 계산하는 것이 좋습니다. 그렇지 않으면 시간초과가 뜨기 쉬워보입니다.... 반성중.

***

### 11050. 이항 계수 1

problem : https://www.acmicpc.net/problem/11050

status : **solved**

code :
```
import sys

n, k = map(int, sys.stdin.readline().split())
p = 1

for i in range(1, k+1) :
    p = p * (n - i + 1) // i
print(p)
```

note : 
* 매우 간단한 수학 문제.

***

### 11866. 요세푸스 문제 0

problem : https://www.acmicpc.net/problem/11866

status : **solved**

code :
```
import sys

n, k = map(int, sys.stdin.readline().split())
queue = list(range(1, n+1))

print('<', end='')
while len(queue) > 1 :
    for _ in range(k-1) : 
        queue.append(queue.pop(0))
    print(queue.pop(0), end=', ')
print(queue.pop(0),'>',sep='')
```

note : 요제푸스 순열 = 큐....왜 이게 바로바로 생각이 안났지

***

### 1436. 영화감독 숌

problem : https://www.acmicpc.net/problem/1436

status : **solved**

code : 
```
n = int(input())

i = 0
num = 666

while True:
    tmp = num
    while tmp >= 666 :
        if tmp % 1000 == 666 :
            i += 1
            break
        else :
            tmp = tmp // 10
    
    if i == n : break
    num += 1

print(num)
```

note :
* brute force 문제. 일차원적인 접근부터 생각해볼것.

***

### 1654. 랜선 자르기

problem : https://www.acmicpc.net/problem/1654

status : **solved**

code :
```
import sys

k, n = map(int, sys.stdin.readline().split())
k_lst = [int(sys.stdin.readline()) for _ in range(k)]

max_k = max(k_lst)

def search(start, end, lst, n):
    mid = (start + end) // 2
    if start > end : 
        return end
    cnt = sum([x//mid for x in k_lst])
    
    if cnt >= n :        
        return search(mid+1, end, lst, n)
    else :
        return search(start, mid-1, lst, n)


print(search(1, max_k, k_lst, n))
```

note : 
* 이분 탐색 및 매개탐색 문제.
* 난이도 하. 그런데 시간이 예상보다 오래 걸림. 익숙해질 필요 있음.
* zerodivisionerror는 생각도 못했는데... start를 1로 해야 함
  * 반례 : [0,1]일때 mid = (0 + 1) // 2 = 0. zero division 

***

### 1874. 스택 수열

problem : https://www.acmicpc.net/problem/1874

status : **solved**

code :
```
import sys

n = int(sys.stdin.readline())
r = 1
chk = False

stk = []
pm = []

for i in range(n) :
    num = int(sys.stdin.readline())
    while r <= num :
        stk.append(r)
        r += 1
        pm.append('+')

    if stk[-1] == num :
        stk.pop()
        pm.append('-')
 
    else :
        chk = True
        break

if chk :
    print('NO')
else :
    for x in pm : print(x)

```
note :
* 오늘 문제 중에 제일 헤맸다. 
* 사실 기본 알고리즘 구성은 빠르게 끝났지만, input을 한번에 받아 구성하는 code 작성 시 typeerror가 자꾸 반복된다.
* 하지만 전체적인 알고리즘을 그대로 두고 input을 그때그때 받아오게 되는 위 코드로 변경시 정답으로 인정되었다.
* 도대체 무엇이 문제였는지... 아직도 배울 점이 많아 보인다.

***

### 1929. 소수 구하기

problem : https://www.acmicpc.net/problem/1929

status:

code :
* trial 1
```
import math

a, b = map(int, input().split())
for i in range(a, b+1):
    if i == 1 : continue
    chk = True
    for j in range(2, math.floor(math.sqrt(i))+1):
        if i % j == 0 :
            chk = False
            break
    if chk : print(i)
```
memory : 126332 kb, time : 948 ms (pypy3)

* trial 2
```
a, b = map(int, input().split())
lst = list(range(0, b+1))
lst[0] = 0
lst[1] = 0

cur = 0

while cur < b:
    if lst[cur] != 0 :
        n = lst[cur]*2
        while n <= b :
            if lst[n] != 0 :
                lst[n] = 0
            n += lst[cur]
    cur += 1

for x in lst :
    if x != 0 and x >= a : print(x)
```
memory : 133176 kb, time : 172 ms (pypy3)

note :
* trial 1은 처음에 실패할 것을 예상하고 풀이했는데 의외로 맞아서 놀랐다. 위 코드의 경우 일일히 숫자 하나씩을 풀기 때문에, 각종 편법들(루트값까지만 계산하기, 도중에 소수가 아니라고 판명되면 그만두기, 1은 통과시키기)을 동원하고도 시간 초과가 뜰 줄 알았다. 맞았으니 그냥 넘어갈 수 도 있겠지만 두 번째 방법을 시도해보기로 하였다.
* 아마 trial 2가 모범답안으로 예상된다. trial 2는 에라스토테네스의 체 기법을 이용했다. 실제로도 훨씬 time이 줄어든 것을 확인할 수 있다. 시간복잡도가 위에 비해 매우 낮기 때문이다.  인 반면 (중복되는 수는 계산에서 제외한다). 위는 O(N^(3/2)), 아래는 O(NloglogN)의 복잡도를 가진다(출처 : 위키피디아) 소수를 다루는 문제에서는 2의 계산법이 좀 더 효율적이라 예상한다.

***

### 1966. 프린터 큐

problem : https://www.acmicpc.net/problem/1966

status : **solved**

code :

```
import sys

l = int(input())

for _ in range(l) :
    n, m = map(int, sys.stdin.readline().split())
    raw_lst = [x for x in map(int, sys.stdin.readline().split())]
    prt_lst = sorted(raw_lst, reverse=True)
    n_lst = [(i, x) for i, x in enumerate(raw_lst)]
    
    cnt = 0
    
    while n_lst:
        idx, prt = n_lst[0]
        if prt >= prt_lst[0] :
            cnt += 1
            prt_lst.pop(0)
            n_lst.pop(0)
            if idx == m : break
        else :
            n_lst.append(n_lst.pop(0))

    print(cnt)
```
note :
* 프라이어티를 따로 sort해서 저장하면 풀이가 쉽습니다.

***

### 2108. 통계학

problem : https://www.acmicpc.net/problem/2108

status : **solved**

code : 
```
from collections import Counter
import sys

def most_frequent(lst):
    cnt = sorted(Counter(lst).items(), key=lambda x:(-x[1], x[0]))

    if len(cnt) > 1 :
        if cnt[1][1] == cnt[0][1] :
            return cnt[1][0]

    return cnt[0][0]

n = int(input())
lst = [x for x in map(int, sys.stdin.readlines())]
s_lst = sorted(lst)

print(round(sum(lst)/n))
print(s_lst[n//2])
print(most_frequent(lst))
print(s_lst[-1] - s_lst[0])
```

note :
 * attribute error때문에 당황. readlines 에 split method 를 붙여서 벌어진 일.
 * 최빈값이 핵심. 따로 함수를 구현해줘야 했다.

***

### 2231. 분해합

problem : https://www.acmicpc.net/problem/2231

status : **solved**

code :
```
n = int(input())
l = len(str(n))
ctr = True

for i in range(max(1, n - 9*l), n) :
    j = sum([x for x in map(int, str(i))]) + i
    if j == n :
        ctr = False
        print(i)
        break
        
    
if ctr : print(0)

```
note : 
* 브루트포스로 풀 수도 있겠지만, 범위 제한이 가능하다. 분해합을 할 때 더해지는 최댓값은 (자릿수) * 9가 되므로, 탐색범위를 크게 제한할 수 있다.

***

### 2292. 벌집

problem : https://www.acmicpc.net/problem/2292

status : **solved**

code : 
```
n = int(input())
i = 0
while True:
    j = 1 + sum([_ for _ in range(1, i+1)]) * 6
    if j >= n :
        print(i+1)
        break
    i += 1
```

note :
* 편의상 list를 만들고 그 합을 구하는 식을 썼는데, 그냥 변수 몇 개를 가지고도 풀 수 있을듯.

***

### 2775. 부녀회장이 될테야

problem : https://www.acmicpc.net/problem/2775

status : **solved**

code :
```
i = int(input())
for _ in range(i):
    k = int(input())
    n = int(input())
    lst = [[0]*n for _ in range(k)]
    lst[0] = list(range(1, n+1))
    for j in range(1, k):
        for l in range(n):
            lst[j][l] = sum(lst[j-1][:l+1])
    print(sum(lst[-1]))
```
note : 간단한 문제라 알고리즘을 구하지 않고 조건을 따라가서 풀음.

***

### 2839. 설탕 배달

problem : https://www.acmicpc.net/problem/2839

status : **solved**

code :
```

n = int(input())
flg = True
for i in range(n // 5, -1, -1):
    if (n - 5*i) % 3 == 0:
        flg = False
        print(i + (n - 5*i) // 3)
        break
if flg : print(-1)

```
note :

***

### 2869. 달팽이는 올라가고 싶다

problem : https://www.acmicpc.net/problem/2869

status : **solved**

code :
```
import math

a, b, v = map(int, input().split())
print( math.ceil((v - a) / (a - b)) + 1)
```

note :
* 기본 수학 문제. 브루트포스는 극단적인 케이스에서 시간 초과를 일으킬 가능성이 높다.

***

### 4949. 균형잡힌 세상

problem : https://www.acmicpc.net/problem/4949

status : **solved**

code :
```
import sys

while True:
    s = sys.stdin.readline()
    if s[0] == '.' and len(s) == 2: break
    stk = []
    flg = False
    
    for i in s :
        if i == '.' : break
        if i == '(' or i == '[' :
            stk.append(i)
        elif i == ')' or i == ']':
            if not stk :
                flg = True
                break
            if ((stk[-1] == '[' and i ==']') or
                (stk[-1] == '(' and i ==')')) :
                stk.pop()
            else :
                flg = True
                break
    if stk : flg = True 

    print('no' if flg else 'yes')
```

note : 

*** 

### 7568.덩치

problem : https://www.acmicpc.net/problem/7568

status : **solved**

code :
```
n = int(input())
lst = [[x for x in map(int, input().split())] for _ in range(n)]
s = [1] * n

for i in range(n):
    for j in lst:
        if lst[i][0] < j[0] and lst[i][1] < j[1] :
            s[i] += 1
print(*s)
```

note :
* 문제를 가끔씩은 쉽게 생각해보자.
    
***

### 10773. 제로

problem : https://www.acmicpc.net/problem/10773

status : **solved**

code :
```
n = int(input())
stk = []
for _ in range(n):
    i = int(input())
    if i == 0 : stk.pop()
    else : stk.append(i)
print(sum(stk))
```
note : 
* 기본 스택 문제

***

### 10989. 수 정렬하기

problem : https://www.acmicpc.net/problem/10989

status : **solved**

code:
* trial 1 
```
import sys

def qsort(lst) :
    if len(lst) <= 1 : return lst
    l_lst = []
    r_lst = []
    m = lst[0]
    
    for x in lst[1:]:
        if x < m :
            l_lst.append(x)
        else :
            r_lst.append(x)
    
    return qsort(l_lst) + [m] + qsort(r_lst)
    
n = int(input())
lst = [x for x in map(int, sys.stdin.readlines())]
print(*qsort(lst), sep='\n')
```
메모리 초과

* trial 2
```
import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    i = int(sys.stdin.readline())
    if not lst : lst.append(i)
    else :
        for j in range(len(lst)):
            if i <= lst[j] :
                lst.insert(j, i)
                break
            if j == len(lst) - 1:
                lst.append(i)
print(*lst, sep='\n')
```
시간 초과

* trial 3 :
```
import sys

n = int(sys.stdin.readline())
lst = [0] * (10001)

for _ in range(n):
    i = int(sys.stdin.readline())
    lst[i] += 1
    
for i in range(10001) :
    if lst[i] > 0:
        for _ in range(lst[i]):
            print(i)
```
memory : 30860 kb, time : 9712

note :
* 극단적으로 시간과 메모리가 제약된 상황. 데이터를 저장하지 않고 count할 때 사용하는 것이 관건이었다.

***

### 11651. 좌표

problem : https://www.acmicpc.net/problem/11651

status : **solved**

code :
```
import sys

n = int(input())
lst = [[ x for x in map(int, sys.stdin.readline().split())] for _ in range(n)]
lst.sort(key = lambda x : (x[1], x[0]))

for i in lst :
    print(i[0], i[1])
```

note :

***

### 15829 : Hashing

problem : https://www.acmicpc.net/problem/15829

status : **solved**

code :

```
l = int(input())
s = input()

h = 0
for i in range(l) :
    h += ( ord(s[i]) - ord('a') + 1 ) * (31 ** i)
h = h % 1234567891

print(h)
```

note :

***

### 18111. 마인크래프트

problem : https://www.acmicpc.net/problem/18111

status : **solved**

code :
```
import sys

n, m, b = map(int, input().split())
lst = [[x for x in map(int, input().split())] for _ in range(n)]
start = min(map(min, lst))
end = max(map(max, lst))
s_lst = sum(map(sum, lst))
t, h = sys.maxsize, -1

def bsearch(start, end, r):
    if start > end:
        return r

    mid = (start + end) // 2
    cnt = 0

    if s_lst - n * m * mid + b < 0 :
        return bsearch(start, mid-1, r)

    else :
        for i in lst:
            for j in i:
                if j > mid :
                    cnt += (j - mid) * 2
                elif j < mid :
                    cnt += mid - j
        if cnt < r[0] or (cnt == r[0] and mid > r[1]) :
            r = (cnt, mid)
        l_r = bsearch(start, mid-1, r)
        r_r = bsearch(mid+1, end, r)

        return r_r if r_r[0] < l_r[0] or (r_r[0] == l_r[0] and r_r[1] > l_r[1]) else l_r
    
result = bsearch(start, end, (t,h))

print(result[0], result[1])
```

note :
* 조건이 있는 binary search로도 풀 수 있고, 브루트 포스로도 풀 수 있다. 전자로 풀이하였으나 조건이 명확(0 < height < 256) 하기에 후자로도 접근 가능하다.

***

### 1260. DFS와 BFS

problem : https://www.acmicpc.net/problem/1260

status : **solved**

code :
```
import sys

n, m, f = map(int, sys.stdin.readline().split())
e = [[0]*n for _ in range(n)]
v = [0]*n
e_b = [[0]*n for _ in range(n)]
v_b = [0]*n
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    e[x-1][y-1] += 1
    e[y-1][x-1] += 1
    e_b[x-1][y-1] += 1
    e_b[y-1][x-1] += 1

s = [f-1]
q = [f-1]
    
while s:    ### DFS
    i = s.pop()
    if v[i] > 0 : continue
    v[i] += 1
    print(i+1, end=' ')
    for j in reversed(range(n)) :
        if e[i][j] > 0 :
            while e[i][j] > 0 :
                s.append(j)
                e[i][j] -= 1
                e[j][i] -= 1
print('')

while q:    ### BFS
    i = q.pop(0)
    if v_b[i] > 0 : continue
    v_b[i] += 1
    print(i+1, end=' ')
    for j in range(n) :
        if e_b[i][j] > 0 :
            while e_b[i][j] > 0 :
                q.append(j)
                e_b[i][j] -= 1
                e_b[j][i] -= 1
    
```

note :
* BFS, DFS 개념 체크. BFS는 큐, DFS는 스택을 이용한다는 점을 기억해두자.

***

### 1389. 케빈 베이컨의 6단계 법칙

problem : https://www.acmicpc.net/problem/1389

status : **solved**

code :
```
import sys

n, m = map(int, sys.stdin.readline().split())
e = [[1e7]*n for _ in range(n)]
for _ in range(m) : 
    x, y = map(int, sys.stdin.readline().split())
    e[x-1][y-1] = min(1, e[x-1][y-1])
    e[y-1][x-1] = e[x-1][y-1]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if e[i][k] + e[k][j] < e[i][j] :
                e[i][j] = e[i][k] + e[k][j]

min_value = 1e7

for i in range(n) :
    if min_value > sum(e[i]) :
        min_value = sum(e[i])
        min_idx = i

print(min_idx+1)

```

note :
* 플로이드 와샬 알고리즘의 좋은 예제.

***

### 1541. 잃어버린 괄호

problem : https://www.acmicpc.net/problem/1541

status : **solved**

code : 
```
import re
s = input()

m = map(int, re.split('[^0-9]', s))
n = re.findall('[^0-9]', s)
t = m.pop(0)

for i in n :
  if i == '-' :
      t -= sum(m)
      break
  t += m.pop(0)

print(t)
```

note :
* 알고리즘 분류에 그리디 알고리즘이 포함되어 있었는데, 글쎄...

***

### 1676. 팩토리얼 0의 개수

problem : https://www.acmicpc.net/problem/1676

status : **solved**

code :
```
n = int(input())
t, f = 0, 0

for i in range(1, n+1):
    while i > 1: 
        if i % 2 == 0:
            t += 1
            i /= 2
        elif i % 5 == 0:
            f += 1
            i /= 5
        else : 
            break
print(min(t, f))
```

note :

***

### 1780. 종이의 개수

problem : https://www.acmicpc.net/problem/1780

status : **solved**

code :
```
import sys

n = int(sys.stdin.readline())
m = [[x for x in map(int, sys.stdin.readline().split())] for _ in range(n)]
r = [0]*3

def check(lst):
    start = lst[0][0]
    for i in lst:
        for j in i:
            if start != j :
                return False
    return True

def div_con(lst, num):
    if num == 1:
        r[lst[0][0] + 1] += 1
        return
        
    if check(lst):
        r[lst[0][0] + 1] += 1
        return 
    else :
        n_num = num // 3
        for i in range(3):
            for j in range(3):
                n_lst = [row[n_num*j:n_num*(j+1)] for row in lst[n_num*i:n_num*(i+1)]]
                div_con(n_lst, n_num)
        return

div_con(m, n)
print(*r, sep='\n')
```
note :
* 분할정복, 재귀의 기본 문제격. 조금 해멨던 나 자신에게 반성하자...

***

### 1992. 쿼드트리

problem : https://www.acmicpc.net/problem/1992

status : **solved**

code :
```
import sys

n = int(sys.stdin.readline())
m = [[x for x in map(int, sys.stdin.readline().strip())] for _ in range(n)]

def div_con(lst, num):
    if num <= 1 :
        return str(lst[0][0])
    
    chk = sum(map(sum, lst))
    if chk ==  0 or chk == num ** 2 :
        return str(lst[0][0])
    else :
        n_num = num // 2
        tmp = '('
        for i in range(2):
            for j in range(2):
                tmp += div_con([row[n_num*j:n_num*(j+1)] for row in lst[n_num*i:n_num*(i+1)]], n_num)
        return tmp + ')'

print(div_con(m, n))
```
note :
*  바로 위 문제와 동일 풀이법.

*** 

### 2178. 미로 탐색

problem : https://www.acmicpc.net/problem/2178

status : **solved**

code :
```
import sys
n, m = map(int, sys.stdin.readline().split())
v = [[0]*m for _ in range(n)]
e = [[x for x in map(int, sys.stdin.readline().strip())] for _ in range(n)]

q = [(0,0,1)]
while q :
  x, y, d = q.pop(0)
  if v[y][x] > 0 : continue
  elif y == n-1 and x == m-1 :
      print(d)
      break
  v[y][x] += 1
  for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
      if x+dx < 0 or x+dx > m-1 or y+dy < 0 or y+dy > n-1 : continue
      elif e[y+dy][x+dx] == 0 : continue
      q.append((x+dx, y+dy, d+1))

```

note :
* BFS 문제의 일종.

***

### 2579. 계단 오르기

problem : https://www.acmicpc.net/problem/2579

status : **solved**

code :
* trial 1 ( Non-DynamicProgramming )
```
import sys

n = int(sys.stdin.readline())
m = [0] + [x for x in map(int, sys.stdin.readlines())]

def gsearch(p, cnt):
    if p == n :
        return m[p]
    elif p == n-1 :
        return m[p] + gsearch(p+1, cnt+1) if cnt == 1 else -1
    else :
        if cnt == 1:
            return m[p] + gsearch(p+2, 0)
        else :
            return m[p] + max(gsearch(p+1, cnt+1), gsearch(p+2, 0))

print(gsearch(0, 0))
    
```
* trial 2(Dynamic Programming)
```
import sys

n = int(sys.stdin.readline())
m = [x for x in map(int, sys.stdin.readlines())]
m_lst = [[] for _ in range(n)]

for i in range(n):
    if i == 0:
        m_lst[i].append((m[i], 0))
    elif i == 1:
        m_lst[i].append((m[i], 0))
        m_lst[i].append((m[i]+m[i-1], 1))
    else :
        for lst in m_lst[i-1] :
            if lst[1] == 1 : continue
            m_lst[i].append((lst[0] + m[i], 1))
        val = -1
        for lst in m_lst[i-2] :
            val = max(lst[0], val)
        m_lst[i].append((val + m[i], 0))

val = -1
for lst in m_lst[-1]:
    val = max(lst[0], val)
print(val)
    
```

note :
* 기본적인 DP 문제. 단순히 분할정복으로 풀게 되면 메모리 문제가 발생한다.

***

### 2667. 단지번호붙이기

problem : https://www.acmicpc.net/problem/2667

status : **solved**

code :
```
import sys

n = int(sys.stdin.readline())
m = [[x for x in map(int, sys.stdin.readline().strip())] for _ in range(n)]
v = [[0]*n for _ in range(n)]
c_lst = []

for y in range(n) :
    for x in range(n) :
        if m[y][x] == 1 and v[y][x] == 0 :
            q = [(x, y)]
            cnt = 0
            while q:
                ax, ay = q.pop(0)
                if v[ay][ax] > 0 : continue
                v[ay][ax] += 1
                cnt += 1
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if ax + dx < 0 or ax + dx > n-1 or ay + dy < 0 or ay + dy > n-1 :
                        continue
                    if m[ay+dy][ax+dx] == 0 :
                        continue
                    q.append((ax+dx, ay+dy))
            c_lst.append(cnt)
print(len(c_lst), *sorted(c_lst), sep='\n')
```

note :
* 문제 자체가 어려웠다기보다는 자잘한 실수가 많았던 문제.

***

### 5525. IOIOI

problem : https://www.acmicpc.net/problem/5525

status : **solved**

code :
* trial 1
```
n = int(input())
m = int(input())
s = input()
p = 'I' + 'OI'*n
cnt = 0

for i in range(m - 2*n):
    if s[i:i+2*n+1] == p : cnt += 1
print(cnt)
```
부분 성공(subtask 2 시간 초과)

* trial 2
```
n = int(input())
m = int(input())
s = input()
cnt = 0
pnt = 0

while pnt < m - 2*n :
    if s[pnt] == 'I':
        t_cnt = 0
        pnt += 1
        while pnt <= m - 2:
            if s[pnt:pnt+2] == 'OI' :
                t_cnt += 1
                pnt += 2
            else :
                break
        if t_cnt >= n :
            cnt += t_cnt-n+1
    else :
        pnt += 1
print(cnt)
```
성공

note :
* 단순히 문자열을 차례대로 비교하게 되면 중복하여 정보를 읽어들이므로, 이미 읽은 정보는 최대한 배제하는 탐색 기법을 생각해보아야 한다.

***

### 6064. 카잉 달력

problem : https://www.acmicpc.net/problem/6064

status : **solved**

code :
* trial 1
```
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    flg = True
    for k in range(1, m*n+1):
        if k % m == x % m and k % n == y % n:
            print(k)
            flg = False
            break
    if flg : print(-1)
```
시간 초과

* trial 2
```
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    flg = True
    k = x if m > n else y
    while k <= m*n :
        if k % n == y % n:
            print(k)
            flg = False
            break
        k += m
    if flg : print(-1)
```
note : 
* 발상의 전환이 필요한 문제.
* 중국인의 나머지 정리를 어떻게 적용시켜봐야 할 지는 생각해볼 것.

***

### 9375. 패션왕 신해빈

problem : https://www.acmicpc.net/problem/9375

status : **solved**

code :
* non dictionary ver.
```
import sys
for _ in range(int(sys.stdin.readline())):
    dic = []
    for _ in range(int(sys.stdin.readline())):
        m, n = sys.stdin.readline().split()
        if not dic :
            dic.append([1, n])
        else :
            flg = True
            for i in dic:
                if i[1] == n :
                    flg = False
                    i[0] += 1
                    break
            if flg :
                dic.append([1, n])
    if not dic : print(0)
    else :
        ans = 1
        for i in dic: ans *= i[0]+1
        print(ans - 1)
```
* dictionary ver.
```
import sys
for _ in range(int(sys.stdin.readline())):
    dic = {}
    for _ in range(int(sys.stdin.readline())):
        m, n = sys.stdin.readline().split()
        if n in dic:
            dic[n] += 1
        else :
            dic[n] = 1
    if not dic : print(0)
    else :
        ans = 1
        for i in dic.values(): ans *= i+1
        print(ans - 1)
```

note :

***

### 9461. 파도반 수열

problem : https://www.acmicpc.net/problem/9461

status : **solved**

code :
```
p = [0] * 100
for i in range(100):
    if i < 3 :
        p[i] = 1
    elif i < 5:
        p[i] = 2
    else :
        p[i] = p[i-5] + p[i-1]

for _ in range(int(input())):
    print(p[int(input())-1])
```

note :

***

### 11047. 동전 0

problem : https://www.acmicpc.net/problem/11047

status : **solved**

code:
```
n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]
cnt = 0
for i in reversed(lst):
    cnt += k // i
    k %= i
    if k == 0 : break
print(cnt)
```

note : 

***

### 11286. 절댓값 힙

problem : https://www.acmicpc.net/problem/11286

status : **solved**

code:
```
import sys
import heapq
q = []

for _ in range(int(sys.stdin.readline())):
    i = int(sys.stdin.readline())
    if i != 0:
        heapq.heappush(q, (abs(i), i))
    else :
        if not q :
            print(0)
        else :
            j = heapq.heappop(q)
            print(j[1])
            while True:
                if not q or q[0] != j[0] : break
                print(heapq.heappop(q)[1])
```

note :
* priority queue를 직접 구현해보는게 가장 실력향상에 도움이 될 듯.

***

### 11403. 경로 찾기

problem : https://www.acmicpc.net/problem/11403

status : **solved**

code :
```
n = int(input())
lst = [[x for x in map(int, input().split())] for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if lst[i][j] > 0 : continue
            if lst[i][k]*lst[k][j] > 0 : lst[i][j] = 1
for i in lst :
    print(*i, sep=' ')
```

note : 
* 플로이드 와샬 알고리즘.

***

### 11659. 구간 합 구하기 4

problem : https://www.acmicpc.net/problem/11659

status : **solved**

code :
```
import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
s_lst = [0] * n
for i in range(n):
    s_lst[i] = lst[i] if i == 0 else lst[i] + s_lst[i-1]
 
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(s_lst[j-1] if i == 1 else s_lst[j-1] - s_lst[i-2])
```

note :
* 간단한 누적합 문제.
