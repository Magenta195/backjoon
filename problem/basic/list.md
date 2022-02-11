
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
    
   
