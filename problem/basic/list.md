
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

### 10998 : A x B

problem : https://www.acmicpc.net/problem/10998

status : **solved**

code : 
```
a, b = map(int, input().split())
print(a*b)
```

note :
