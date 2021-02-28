# 03 for문

## Summary

### **함수**

- range()

> range(*start*, *stop*, *step*)<br>
 입력 파라미터로는 int(정수형)만 받을 수 있으며, range타입으로 반환된다.<br>
 start부터 시작하여 stop의 바로 앞까지 step의 간격으로 변화하는 정수의 배열을 나타낸다.<br>

> range(int) : 입력 파라미터가 하나인 경우 stop을 의미하고, start는 0, step은 1로 기본값이 설정되어있다.<br>
 range(int, int) : 입력 파라미터가 두개인 경우 start, stop을 의미하고, step은 1로 기본값이 설정되어있다.<br>

### **반복문**

- for문

> for 변수 in 순서열:
&nbsp;&nbsp;&nbsp;&nbsp;수행할 문장들<br>

> for문의 기본 구조는 위와 같다. for와 in이 기본적으로 사용되고 가운데 변수 마지막에 순서열이 나온다. 순서열에는 일반적으로 리스트, 튜플, 문자열, range타입 등과 같은 타입이 사용된다. 이러한 경우에 순서열의 데이터를 하나씩 읽어와 변수에 할당해준 후 아래의 코드 블록을 수행하게 된다.<br>
 이 외에도 enumerate(), dict타입, 순서열 안에 순서열이 있는 형태(2차원 배열) 등과 같은 경우에, 변수 부분에 여러 변수를 넣어 한번에 여러 값을 할당받아 아래 코드 블록을 수행하도록 만들어 줄 수 있다.<br>

<br>

### **문자열**

- .format()

> 문자열 안에 어떤 값을 삽입해 문자열을 포매팅해준다. 즉, 문자열 중간 중간에 특정 변수의 값을 넣어주기 위해 많이 사용된다.<br>
 유용하게 사용되는 몇가지 기능을 아래의 예시를 참고하여 알아보자.<br>
 1. 기본적인 포매팅<br>
 문자열 사이의 { }에 format 입력 파라미터를 순서대로 넣어준다.
 2. 인덱스를 이용한 포매팅<br>
 문자열 사이의 {index}에 index에 맞게 입력 파라미터를 넣어준다.
 3. 이름을 이용한 포매팅<br>
 문자열 사이의 {name}에 name에 맞게 입력 파라미터를 넣어준다.
 4. 문자열 정렬<br>
 {:N}을 통해 문자열의 총 자릿수를 N칸으로 하고 <, >, ^ 을 이용해 각각 왼쪽, 오른쪽, 가운데 정렬을 해줄 수 있다.
 5. 공백 채우기<br>
 문자열 정렬을 할때 : 와 정렬방향 사이에 값을 넣어 공백을 다른 값으로 채울 수 있다.
 6. 소수점 표현<br>
 {:.Nf}을 통해 소수점 아래에 대하여 자릿수를 N칸으로 설정해줄 수 있다.
 7. 종합하여 사용하기<br>
 위의 기능들은 함께 사용이 가능하다.<br>
 { } 내에 첫번째로 index/name, 두번째로 :, 세번째로 공백 채울 값, 네번째로 정렬방향, 다섯번째로 전체 자릿수, 여섯번째로 .소수점 아래 자릿수f 를 입력해주면 된다.
 8. 중괄호 { } 표현<br>
 {{}}와 같이 중괄호를 중복으로 사용하여 포매팅 역할이 아닌 중괄호로 표현이 가능하다.
 
```
>>> print("포매팅을 {} 이러한 문자열이 {}.".format("이용하면", "완성된다"))
포매팅을 이용하면 이러한 문자열이 완성된다.

>>> print("포매팅을 {1} 이러한 문자열이 {0}.".format("이용하면", "완성된다"))
포매팅을 완성된다 이러한 문자열이 이용하면.

>>> print("저는 {name}이고, {age}살입니다.".format(name = "최윤성", age = 25))
저는 최윤성이고, 25살입니다.

>>> print("문자열 정렬은 {:>10} 이렇게 사용한다.".format("Hello"))
문자열 정렬은      Hello 이렇게 사용한다.

>>> print("공백 채우기는 {:0^10} 이렇게 사용한다.".format("Hello"))
공백 채우기는 00Hello000 이렇게 사용한다.

>>> print("소수점 표현 {:.2f}".format(123.4567))
소수점 표현 123.46

>>> print("종합하여 사용하면 {number:-^10.3f} 이와 같다.".format(number = 123.45))
종합하여 사용하면 -123.450-- 이와 같다.

>>> print("{{}}를 포매팅과 {} 출력하기".format("함께"))
{}를 포매팅과 함께 출력하기
```

<br>

---

# *Source Code*

## 01 구구단

```python
N = int(input())  # N : 구구단의 단을 입력 받음

for i in range(1, 10):  # i에 1, 2, 3, ... , 8, 9까지 할당하며 아래의 동작 수행
    print("{} * {} = {}".format(N, i, N*i))  # {}에 format()내의 값들을 차례로 하나씩 넣어줌
```

## 02 A+B (3)

```python
T = int(input())  # T : 테이스 케이스의 개수를 입력받음

for i in range(T):  # T번 반복
    A, B = map(int, input().split())  # A, B : 덧셈 연산을 수행할 두 정수를 입력받음
    print(A+B)
```

## 03 합

```python
n = int(input())  # n : 합할 수의 마지막 값을 입력받음
result = 0  # result : 합한 최종 결과

for i in range(1, n+1):  # 1부터 n까지.
    result += i  # result = result + i
    
print(result)
```

## 04 빠른 A+B

```python
# input() 보다 sys.stdin.readline()이 빠르다
# 시간 복잡도가 커질수록 차이는 커지게 된다.

import sys  # sys 모듈을 불러옴

T = int(input())  # T : 테스트 케이스의 개수

for i in range(T):  # T번 반복
    n, m = map(int, sys.stdin.readline().split())  # n, m : 한 줄씩 문자열을 입력받아 공백, tab, 줄바꿈을 기준으로 나눠 할당
    print(n+m)
```

## 05 N 찍기

```python
N = int(input())  # N : 출력하고자하는 자연수의 마지막값

for i in range(1, N+1):  # N번 반복 (i는 1부터 N까지)
    print(i)
```

## 06 기찍 N

```python
N = int(input())  # N : 출력하고자하는 자연수의 마지막값

for i in range(N):  # N번 반복 (i는 0부터 N-1까지)
    print(N - i)

# for i in range(N, 0, -1):  # N번 반복 (i는 N부터 1까지 -1씩 변화)
#     print(i)
```

## 07 A+B (7)

```python
T = int(input())  # T : 테이트 케이스 개수

for i in range(1, T+1):  # T번 반복. i : 1 ~ T
    n, m = map(int, input().split())
    print("Case #{}: {}".format(i, n+m))  # " ".format() : 문자열에 .format을 통해 {}부분에 원하는 내용을 삽입가능
```

## 08 A+B (8)

```python
T = int(input())  # T : 테스트 케이스 개수

for i in range(1, T+1):  # T번 반복. i : 1 ~ T
    n, m = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i, n, m, n+m))  # " ".format() : 문자열에 .format을 통해 {}부분에 원하는 내용을 삽입가능
```

## 09 별 찍기 (1)

```python
N = int(input())  # N : 출력할 별의 줄 수

for i in range(1, N+1):  # N번 반복. i : 1 ~ N
    print("{}".format("*"*i))  # " ".format() : 문자열에 .format을 통해 {}부분에 원하는 내용을 삽입가능
```

## 10 별 찍기 (2)

```python
N = int(input())  # N : 출력할 별의 줄 수

for i in range(1, N+1):  # N번 반복. i : 1 ~ N
    print("{}".format(" "*(N-i) + "*"*i))  # " ".format() : 문자열에 .format을 통해 {}부분에 원하는 내용을 삽입가능
```

## 11 X보다 작은 수

```python
N, X = map(int, input().split())  # N, X : 입력받을 정수의 개수, 기준이 되는 수
lst = list(map(int, input().split()))  # 입력받은 수들을 lst에 할당

for i in range(N):  # N번 반복
    if lst[i] < X:
        print(lst[i], end = " ")  # 출력 후 줄바꿈이 아닌 공백을 출력
```
