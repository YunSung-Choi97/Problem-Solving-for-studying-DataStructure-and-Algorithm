# 17 정수론 및 조합론

|문제 번호|문제 제목|문제 풀이|Memo|
|:---:|---|:---:|---|
|[num01](https://www.acmicpc.net/problem/5086)|title01|[python](01_5086.py)|    |
|[1037](https://www.acmicpc.net/problem/1037)|title02|[python](02_1037.py)|    |
|[2609](https://www.acmicpc.net/problem/2609)|title03|[python](03_2609.py)|    |
|[1934](https://www.acmicpc.net/problem/1934)|title04|[python](04_1934.py)|    |
|[2981](https://www.acmicpc.net/problem/2981)|title05|[python](05_2981.py)|    |
|[3036](https://www.acmicpc.net/problem/3036)|title06|[python](06_3036.py)|    |
|[11050](https://www.acmicpc.net/problem/11050)|title07|[python](07_11050.py)|    |
|[11051](https://www.acmicpc.net/problem/11051)|title08|[python](08_11051.py)|    |
|[1010](https://www.acmicpc.net/problem/1010)|title09|[python](09_1010.py)|    |
|[9375](https://www.acmicpc.net/problem/9375)|title10|[python](10_9375.py)|    |
|[1676](https://www.acmicpc.net/problem/1676)|title11|[python](11_1676-1.py)|    |
|[2004](https://www.acmicpc.net/problem/2004)|title12|[python](12_2004.py)|    |

<br>

## Summary

- 최대공약수 구하기

```python
def gcd(num1, num2):
    if num1 < num2:
        (num1, num2) = (num2, num1)
    while num2 != 0:
        (num1, num2) = (num2, num1 % num2)
    return num1
```

- 약수 구하기
```python
def factor(num):
    factor_list = []

    # 반복문을 num의 제곱근까지만 해줌.
    for Q in range(1, int(num**0.5) + 1):
        if num % Q == 0:
            factor_list.append(Q)
            if Q * Q != num:  # 제곱수인 경우에 같은 수가 두번 입력되는 것을 막기 위함.
                factor_list.append(num//Q)
    factor_list.sort()
    return factor_list
```

- 팩토리얼 구하기 (3가지)

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        answer = 1
        for i in range(1, n+1):
            answer *= i
        return answer
```
```python
factorial = [1 for _ in range(N+1)]
for i in range(1, N+1):
    factorial[i] = i * factorial[i-1]
```
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

첫번째 방법은 반복문을 통해 팩토리얼 값을 계산하여 리턴한다. 두번째 방법은 반복문을 통해 리스트의 인덱스 번호에 해당하는 팩토리얼 값을 저장한다. 세번째는 재귀를 통해 팩토리얼 값을 리턴한다.<br>
세 방법은 조금씩 차이는 있지만, 모두 팩토리얼 값을 구할 수 있다. 첫번째 방법이 좋아보이고, 두번째 방법은 메모리를 크게 사용하게 될 수 있다. 하지만 큰 수들의 팩토리얼 값들을 여러번 사용해야 한다면 두번째 방법이 더 빠를 수 있다.

- n! 인수에 num의 개수 구하기
```python
def num_count(n, num):
    answer = 0
    while n != 0:
        n //= num
        answer += n
    return answer
```

<br>

---

# *Source Code*

## 01 배수와 약수

```python
import sys
input = sys.stdin.readline

while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0:  # 종료 조건
        break

    if num1 % num2 == 0:    # num1이 num2의 배수
        print('multiple')
    elif num2 % num1 == 0:  # num1이 num2의 약수
        print('factor')
    else:                   # 배수/약수 관계가 아님
        print('neither')
```

## 02 약수

```python
import sys
input = sys.stdin.readline

length = int(input())  # 진짜 약수의 개수
factor_lst = list(map(int, input().split()))    # 진짜 약수를 입력받아 리스트에 저장
print(max(factor_lst) * min(factor_lst))        # 진짜 약수 중 (최대값 X 최소값) 출력
```

## 03 최대공약수와 최소공배수

```python
import sys
input = sys.stdin.readline

# 최대공약수를 구하는 함수
def gcd(num1, num2):
    if num1 < num2:
        (num1, num2) = (num2, num1)
    while num2 != 0:
        (num1, num2) = (num2, num1 % num2)
    return num1

N, M = map(int, input().split())

GCD = gcd(N, M)  # N과 M의 최대공약수 GCD

# 최대공약수와 최소공배수 출력 (최소공배수 = N x M / GCD)
print(GCD)
print(N * M // GCD)
```

## 04 최소공배수

```python
import sys
input = sys.stdin.readline

# 최대공약수를 구하는 함수
def gcd(num1, num2):
    if num1 < num2:
        (num1, num2) = (num2, num1)
    while num2 != 0:
        (num1, num2) = (num2, num1 % num2)
    return num1

T = int(input())  # T : 테스트 케이스의 개수

# 테스트 케이스에 대하여, A와 B의 최대공약수 GCD를 구한 후 LCM (A x B / GCD) 출력
for _ in range(T):
    A, B = map(int, input().split())
    GCD = gcd(A, B)
    print(A * B // GCD)
```

## 05 검문

```python
import sys
input = sys.stdin.readline

# 최대공약수를 구하는 함수
def gcd(num1, num2):
    if num1 < num2:
        (num1, num2) = (num2, num1)
    while num2 != 0:
        (num1, num2) = (num2, num1 % num2)
    return num1

# 약수를 구하는 함수
def factor(num):
    factor_list = []

    # 반복문을 num의 제곱근까지만 해줌.
    for Q in range(1, int(num**0.5) + 1):
        if num % Q == 0:
            factor_list.append(Q)
            if Q * Q != num:  # 제곱수인 경우에 같은 수가 두번 입력되는 것을 막기 위함.
                factor_list.append(num//Q)
    factor_list.sort()
    return factor_list

N = int(input())  # 입력받을 수의 개수

num_list = []  # 입력받은 수를 저장하는 리스트
for _ in range(N):
    num_list.append(int(input()))
num_list.sort()

num_dif = []  # 입력받은 수들 사이의 차를 저장하는 리스트 (이웃한 인덱스사이의 차만 저장)
for i in range(N-1):
    num_dif.append(num_list[i+1] - num_list[i])

# "이웃한 수의 차"들의 최대공약수를 구해준 후 약수를 결과에 저장
if N == 2:
    result = factor(num_dif[0])
else:
    GCD = num_dif[0]
    for i in range(1, N-1):
        GCD = gcd(GCD, num_dif[i])
    result = factor(GCD)

# 결과 중 1을 제외한 값을 출력
for M in result[1:]:
    print(M, end=' ')
```

## 06 링

```python
import sys
input = sys.stdin.readline

# 최대공약수를 구하는 함수
def gcd(num1, num2):
    if num1 < num2:
        (num1, num2) = (num2, num1)
    while num2 != 0:
        (num1, num2) = (num2, num1 % num2)
    return num1

N = int(input())

num_list = list(map(int, input().split()))

for i in range(1, N):
    GCD = gcd(num_list[0], num_list[i])
    print('{}/{}'.format(num_list[0] // GCD, num_list[i] // GCD))  # "(num_list[0] // GCD) / (num_list[i] // GCD)" 출력
```

## 07 이항 계수 1

```python
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# (N)! / ((N-K)! * K!)
answer = 1
for i in range(K):
    answer = answer * (N-i) // (i+1)

print(answer)
```

## 08 A이항 계수 2

```python
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# (N)! / ((N-K)! * K!)
answer = 1
for i in range(K):
    answer = answer * (N-i) // (i+1)

print(answer % 10007)
```

## 09 다리 놓기

```python
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    # (M)! / ((M-N)! * N!)
    answer = 1
    for i in range(N):
        answer = answer * (M-i) // (i+1)
    print(answer)
```

## 10 패션왕 신해빈

```python
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    
    clothes = []  # 의상 종류를 저장
    for i in range(n):
        clothes.append(input().split()[-1])
    
    kind = []   # 의상 종류를 저장 (중복X)
    count = []  # 같은 의상 종류의 개수를 저장
    for i in range(n):
        if not clothes[i] in kind:
            kind.append(clothes[i])
            count.append(clothes.count(clothes[i]))
    
    # 전체 = (의상 종류1 개수 + 1) x (의상 종류2 개수 + 1) x ... x (의상 종류k 개수 + 1) - 1  단, 여기서 k는 kind의 크기
    answer = 1
    for i in count:
        answer *= i+1

    print(answer-1)
```

## 11 팩토리얼 0의 개수

풀이 1
```python
import sys
input = sys.stdin.readline

N = int(input())

count = 0   # N > 5^count 를 만족하는 count의 최대값. 즉 5의 거듭제곱 중 가장 큰 수의 지수
N_size = N  # count를 계산하기 위해 N값을 저장
while N_size > 4:
    N_size = N_size // 5
    count += 1

# 숫자의 뒤에 0이 있기위해서는 10의 배수가 되어야한다.
# 10의 배수가 되기위해서는 2 x 5가 있어야하므로 인수로 2와 5가 있어야한다.
# 팩토리얼을 계산하면 2의 개수가 5의 개수가 훨씬 많기때문에 5의 개수를 파악하면 10이 몇번 들어갔는지 알 수 있다.
answer = 0
for i in range(1, count+1):
    answer += N // (5 ** i)
print(answer)

'''
이 문제에서는 0 <= N <= 500이라는 조건이 있기때문에 아래 두 줄의 코드로도 해결이 가능하다.

N = int(input())
print(N//5 + N//25 + N//125)
'''
```

풀이 2
```python
import sys
input = sys.stdin.readline

N = int(input())

def factorial(n):
    if n == 1:
        return 1
    else:
        answer = 1
        for i in range(1, n+1):
            answer *= i
        return answer

# factorial = [1 for _ in range(N+1)]
# for i in range(1, N+1):
#     factorial[i] = i * factorial[i-1]

# N!를 구한 후 문자열로 바꿔 -1 index부터 0의 개수를 확인
number = str(factorial(N))
count = 0
for i in range(-1, -1 * (len(number)+1), -1):
    if number[i] == '0':
        count += 1
    else:
        break
print(count)
```

풀이 3
```python
# 런타임 에러 (RecursionError) 발생
import sys
input = sys.stdin.readline

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

N = int(input())

N_fac = factorial(N)

# 10으로 나눠 나머지가 0인 경우는 끝자리가 0인것을 의미
count = 0
while N_fac % 10 == 0:
    count += 1
    N_fac //= 10
print(count)
```

## 12 조합 0의 개수

```python
import sys
input = sys.stdin.readline

# n! 인수에 num의 개수를 파악하는 함수
def num_count(n, num):
    answer = 0
    while n != 0:
        n //= num
        answer += n
    return answer

n, m = map(int, input().split())

if m == 0:
    print(0)
else: 
    # 2의 개수와 5의 개수 중 작은 값을 정답으로 출력
    print(min(num_count(n, 2)-num_count(m, 2)-num_count(n-m, 2), num_count(n, 5)-num_count(m, 5)-num_count(n-m, 5)))

# 팩토리얼을 계산해서, 또는 조합을 계산해서 문제를 풀게되면 시간초과 혹은 메모리 초과 등의 결과가 나오게 된다.
```