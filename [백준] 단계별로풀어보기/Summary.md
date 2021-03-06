# Summary

단계별로 정리한 Summary를 통합

<br>

## Index

1. **[Syntax Summary](#syntax-summary)**
- [함수](#함수)
> print(), input(), len(), map(), range(), enumerate()<br>
(수학) max() / min(), sum(), round(), math.ceil() / math.floor() / math.trunc()<br>
(아스키코드) ord(), chr()
- [조건문](#조건문)
> if / elif / else 구문
- [반복문](#반복문)
> for문, while문, continue, break
- [에러와 예외 처리](#에러와-예외-처리)
> try, except, raise, else, finally
- [문자열](#문자열)
> .format(), .split(), .strip(), .join()
- [리스트](#리스트)
> .append(), .sort() / sorted(), .index() / .find(), .count()
- [딕셔너리](#딕셔너리)
> .keys() / .values() / .items(), .get(), .update() / .setdefault(), .pop() / .popitem(), .clear(), .copy()
- [집합](#집합)
> .intersection(), .union(), .difference(), .symmetric_difference()
- [순열과 조합](#순열과-조합)
> 순열 / 조합 / 중복 순열 / 중복 조합
- [기타](#기타)
> global

2. **[Algorithm Summary](#algorithm-summary)**
- [소수](#소수)
- [팩토리얼](#팩토리얼)

<br>

---

## Syntax Summary

### 함수

- print()

 > 입력받은 인자를 화면에 출력해 주는 함수<br>
 ','를 이용해 여러 파라미터를 동시에 받을 수 있다.<br>

 > print(value1, value2, sep=value3) : 이와 같이 sep를 이용하면 val1과 val2의 출력사이에 공백이 아닌 val3를 출력할 수 있다. sep는 ' '(공백)으로 기본값이 설정되어있다.<br>
 print(value1, end=value2) : 이와 같이 end를 이용하면 val1을 출력한 후(모든 입력 인자를 출력한 후) 줄바꿈이 아닌 val2를 출력할 수 있다. end는 '\n'(줄바꿈)으로 기본값이 설정되어있다.<br>

<br>

- input()

 > 사용자로부터 입력받은 값을 리턴하는 함수<br>

 > input(value1) : 입력 인자가 있는 경우 val1을 화면에 출력해준 후 사용자로부터 입력을 받는다.<br>

<br>

- len()

 > 순서열의 길이를 반환하는 함수

<br>

- map()

 > 일반적으로 map(함수, 데이터)와 같이 입력 받는다.<br>
 입력받은 데이터에 각각에 대하여 앞의 함수를 적용하여 순서쌍 또는 배열의 형태로 리턴해준다.<br>

<br>

- range()

 > 시작 지점, 끝나는 지점, 간격을 입력받아 range타입의 정수 순서열을 반환한다.

 > range(int) : 입력 파라미터가 하나인 경우 stop을 의미하고, start는 0, step은 1로 기본값이 설정되어있다.<br> 
 range(int, int, int) : 입력 파라미터는 각각 start, stop, step을 의미한다. start부터 stop 이전까지 step 간격으로 변하는 순서열을 반환한다.<br>
 range(int, int) : 입력 파라미터가 두개인 경우 start, stop을 의미하고, step은 1로 기본값이 설정되어있다.<br>

<br>

- enumerate()

> 순서가 있는 자료형을 입력받고, 인덱스와 값을 함께 enumerate 객체로 반환한다.<br>
일반적으로 for문과 함께 자주 사용된다.<br>
list, tuple, dict, string 등을 입력받아 인덱스와 값을 리턴하고, 입력값이 dict형인 경우 인덱스와 key-value를 함께 리턴한다.

<br>

- max() / min()

 > 입력 파라미터 내에서 최댓값/최솟값을 반환하는 함수

<br>

- sum()

 > 입력 파라미터들의 합산값을 반환하는 함수

<br>

- round()

 > 입력 파라미터의 반올림 값을 반환하는 함수<br>
 두번째 값으로 몇번째 자리까지 나타낼지 정해줄 수 있다.

```python
>>> round(3.141592)
3

>>> round(3.141592, 2)
3.14

>>> round(31.41592, -1)
30.0
```

<br>

- math.ceil() / math.floor() / math.trunc()

 > math 모듈을 호출한 뒤 사용가능하다.<br>
 ceil() : 올림 값을 반환하는 함수
 floor() : 내림 값을 반환하는 함수
 trunc() : 0 방향의 가장 가까운 정수를 반환하는 함수 (양수에서 내림, 음수에서 올림)

<br>

- ord()

 > 입력 파라미터로 받은 문자에 대한 아스키 코드값 반환

<br>

- chr()

 > 입력 파라미터로 받은 아스키 코드값에 대한 문자 반환

<br>

### 조건문

- if / elif / else구문

 > if (condition):<br>
 &nbsp;&nbsp;&nbsp;&nbsp;(code block)<br>
 elif (condition):<br>
 &nbsp;&nbsp;&nbsp;&nbsp;(code block)<br>
 else:<br>
 &nbsp;&nbsp;&nbsp;&nbsp;(code block)<br>

 > 각각의 if / elif / else : if와 elif는 조건이 True일 경우 아래의 들여쓰기를 기준으로 형성된 코드블록의 코드를 수행하게 된다. else는 위에서 모든 조건이 False일 경우 마찬가지로 코드블록의 코드를 수행하게 된다.<br>

 > elif와 else는 if 조건문 이후에만 사용할 수 있으며 필요한 경우에만 작성해주면 되고(elif는 여러개가 나타날 수 있음), 위에서부터 조건을 탐색하여 탐색한 조건이 아닌 경우에만 아래로 내려가 조건문으로 다시 들어가는 구조이고 모든 조건에 부합하지 않을 때 else문으로 들어가게 된다.<br>
 즉, ( if (A조건) .. if (B조건) ) != ( if (A조건) .. elif (B조건) )<br>

<br>

### 반복문

- for문

 > for 변수 in 순서열:<br>
 &nbsp;&nbsp;&nbsp;&nbsp;수행할 문장들<br>

 > for문의 기본 구조는 위와 같다. for와 in이 기본적으로 사용되고 가운데 변수 마지막에 순서열이 나온다. 순서열에는 일반적으로 리스트, 튜플, 문자열, range타입 등 다양한 타입이 사용된다. 이러한 경우에 순서열의 데이터를 하나씩 읽어와 변수에 할당해준 후 아래의 코드 블록을 수행하게 된다.<br>
 이 외에도 enumerate(), dict타입, 순서열 안에 순서열이 있는 형태(2차원 배열) 등과 같은 경우에, 변수 부분에 여러 변수를 넣어 한번에 여러 값을 할당받아 아래 코드 블록을 수행하도록 만들어 줄 수 있다.<br>

<br>

- while문

 > while (condition):<br>
 &nbsp;&nbsp;&nbsp;&nbsp;(code block)<br>

 > while문은 while 바로 다음 작성되는 조건에 대하여 조건이 참일 경우 아래 코드블록을 수행하게 된다. 코드블록을 모두 수행한 뒤 다시 조건이 참인지 확인하는 과정으로 돌아간다. 따라서, 어떤 동작을 반복적으로 수행하다가 특정 상황(조건에 맞지 않는 상황)에 중단하고 싶을 때 주로 사용하게 된다.<br>
 조건을 항상 참으로 만들어 무한 루프가 되지 않도록 주의해야한다.

<br>

- continue / break

 > continue/break를 이용하면 반복문을 조금 더 효율적으로 사용할 수 있다.<br>
 반복문 내에서 continue를 만나게 되면 아래의 코드를 통과하고 반복문의 다음 차례로 넘어가게 된다. break를 만나게 되면 아래의 코드를 통과하고 반복문을 끝내게 된다.<br>
 따라서, continue는 주로 특정 상황에 대하여 아래의 동작을 수행하고 싶지않거나 확인할 필요가 없는 경우에 많이 사용한다. break는 주로 무한 루프를 끝내거나 수행하고 싶은 동작을 모두 했을 때 끝내고 넘어가기 위한 방법으로 많이 사용된다.

<br>

### 에러와 예외 처리

- try, except, raise, else, finally

 > try:<br>
 &nbsp;&nbsp;&nbsp;&nbsp;(code block)<br>
 except:<br>
 &nbsp;&nbsp;&nbsp;&nbsp;(code block)<br>

 > 에러가 발생할 가능성이 있는 코드를 try의 코드 블록안에 넣어줌으로서, 에러가 발생했을 때 에러표시와 프로그램 종료가 아닌 원하는 수행동작을 except의 코드 블록에 넣어 에러에 대한 처리가 가능하다.<br>
 추가로, raise를 이용하면 원하는 에러를 발생시킬수 있다. 그리고 except 아래에 else/finally구문을 이용하여 에러가 발생하지 않은 경우/예외 발생 여부와 관계없이 모든 경우에 대하여 수행할 동작을 작성해줄 수 있다.

<br>

### 문자열

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

- .split()

 > 문자열을 나누어준다.<br>
 기본값으로 ' '(공백), '\t'(tab), '\n'(줄바꿈)을 기준으로 문자열을 나눠 리스트 형태로 리턴해준다.<br>
 .split(value1)과 같이 사용하면 val1이 구분자가 된다.<br>

<br>

- .strip()

 > 문자열의 왼쪽과 오른쪽에서 입력 파라미터를 제거한다. 입력 파라미터가 없는 경우 공백(줄바꿈, 탭)을 제거한다.<br>
 rstrip()은 오른쪽에서만, lstrip()은 왼쪽에서만 동일하게 동작한다.

<br>

- .join()

 > '구분자'.join(리스트) 형태로 사용하며, 매개 변수로 전달받은 리스트의 요소와 요소 사이에 구분자를 넣어 하나의 문자열로 합쳐 반환한다.

<br>

### 리스트

- .append()

 > 입력 파라미터를 리스트의 가장 마지막에 추가하는 함수

<br>

- .sort() / sorted()

 > 리스트의 요소를 기본적으로 오름차순으로 정렬해준다.

 > .sort(reverse=True) : 이와 같이 reverse를 이용하면 내림차순으로 정렬된다.<br>
 .sort(key=lambda x:x[1]) : key와 매개변수를 이용하여 정렬하기전 정렬 기준이 되는 key값을 지정할 수 있다. 여기에 함수를 사용하거나, lambda를 통해 간단히 함수를 구현하여 정렬 기준을 설정해줄 수 있다.<br>
 <=> sorted() : 기본적으로 오름차순으로 정렬해주는 동일한 역할을 하는 함수이다. .sort()는 리스트에 대하여 본인을 정렬된 리스트값으로 바꿔주는 함수이고, sorted()는 파라미터로 리스트 뿐만아니라 다양한 순서열을 받을 수 있고 정렬된 리스트를 반환한다.
 
<br>

- .index() / find()

 > 리스트 내에서 입력 파라미터로 받은 요소의 인덱스 값을 반환하는 함수

 > .index(value1, start, end) : 이와 같이 리스트 내에서 찾고자하는 val1을 입력해주고, 범위를 정하고 싶다면 start와 end를 사용해줄 수 있다. val1이 리스트 내에 여러개 존재한다면 첫번째 인덱스를 반환하기때문에, index()에서 start에 index(value1)+1을 넣어 두번째 위치를 찾을 수 있다.<br>
 <=> .find() : 동일하게 리스트 내에서 찾고자하는 값의 인덱스를 반환해주는 함수<br>
 리스트 내에 찾는 값이 없을 경우 index()는 ValueError가 발생하고, find()는 -1을 반환한다.

<br>

- .count()

 > 리스트 내부에 입력 파라미터의 개수를 반환

<br>

### 딕셔너리

- .keys() / .values() / .items()

 > 딕셔너리의 모든 key값과 value값에 대한 정보를 얻을 수 있다.<br>
 keys() : 딕셔너리의 모든 key값을 객체 dict_keys로 반환한다.<br>
 values() : 딕셔너리의 모든 value값을 객체 dict_values로 반환한다.<br>
 items() : 딕셔너리의 모든 key와 value 쌍을 객체 dict_items로 반환한다.

<br>

- .get()

 > key값이 입력 파라미터인 value를 반환한다. 존재하지 않으면 None을 반환한다.<br>
 .get(value1, value2) : val1을 key값으로 하는 value를 반환하고, 존재하지 않는다면 val2를 반환한다.

<br>

- .update() / .setdefault()

 > 딕셔너리에 key-value를 추가하는 함수<br>
 update(*key*=*value*) : 입력받은 key에 대응하는 value값을 수정하고, key가 없다면 key-value 쌍을 추가한다. 또한, 여러 개를 동시에 추가할 수 있다.<br>
 setdefault(*key*, *value*) : 입력받은 key-value 쌍을 추가한다. 입력 파라미터가 하나인 경우 key로 처리되고 value로 None이 저장된다.

<br>

- .pop() / .popitem()

 > 딕셔너리에 key-value를 제거하는 함수<br>
 pop() : 입력받은 key에 대응하는 value값을 반환하고, 딕셔너리에서 key-value를 제거한다. 입력 파라미터가 두개인 경우 key가 딕셔너리 내에 없을 때 두번째 파라미터가 반환값이 된다.<br>
 popitem() : 마지막 key, value 쌍을 반환하고, 딕셔너리에서 제거한다.

<br>

- .clear()

 > 딕셔너리의 모든 key, value를 삭제.

<br>

- .copy()

 > 딕셔너리를 복사하여 반환하는 함수.<br>
 같은 객체가 되지 않으며 복사할 때 사용된다.

<br>

### 집합

- .intersection(), .union(), .difference(), .symmetric_difference()

 > 집합간에 교집합, 합집합, 차집합, 대칭차집합을 계산해준다. 이 외에도 서로소, 포함관계를 확인하는 매소드도 있다.

```python
A = set([1, 2, 3, 4])
B = set([3, 4, 5, 6])
```
```
>>> A.intersection(B)
{3, 4}
>>> A.union(B)
{1, 2, 3, 4, 5, 6}
>>> A.difference(B)
{1, 2}
>>> A.symmetric_difference(B)
{1, 2, 5, 6}
```

<br>

### 순열과 조합

- 순열 / 조합 / 중복 순열 / 중복 조합

> itertools 라이브러리을 이용하면 순열/조합/중복 순열/중복 조합을 간단히 구현해낼 수 있다.

```python
from itertools import permutations  # 순열
from itertools import combinations  # 조합
from itertools import product, repeat  # 중복 순열
from itertools import combinations_with_replacement  # 중복 조합

permutations(range(1, N+1), M)  # N개 중 M개를 정렬
combinations(range(1, N+1), M)  # N개 중 M개를 선택
product(range(1, N+1), repeat=M)  # N개 중 M개를 정렬 (중복 허용)
combinations_with_replacement(range(1, N+1), M)  # N개 중 M개를 선택 (중복 허용)
```

<br>

### 기타

- global

> 지역변수를 전역변수로 사용하고자 할때 global (변수명)과 같이 작성해주면 된다.

<br>

---

## Algorithm Summary

### 소수

- 기본 : 소수의 정의를 그대로 사용

```python
def is_prime(n):  # n이 소수일때 True를 반환하는 함수
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
```

- n의 제곱근까지만 확인하는 방식 : n의 제곱근까지 약수가 없다면 그 이후에도 약수가 존재하지 않는 점을 이용

```python
def is_prime(n):  # n이 소수일때 True를 반환하는 함수
    if n <= 1: return False
    if n == 2: return True
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

- 에라토스테네스의 체 : N보다 작거나 같은 모든 소수를 찾는 알고리즘으로, 여러 개의 수가 소수인지 아닌지 판별할 때 사용하는 방식

```python
# is_prime 리스트의 인덱스 값이 소수인지에 대하여 True/False를 저장
n = 100  # N 값을 통해 확인할 범위 지정
is_prime = [True for _ in range(n+1)]  # 모든 수가 소수(True)인 것으로 초기화
is_prime[0], is_prime[1] = False, False  # 0과 1은 소수가 아니므로 False로 초기화

for i in range(2, int(n**0.5) + 1):  # 2부터 n의 제곱근까지 확인
    if is_prime[i] == True:  # i가 소수인 경우 i의 배수는 소수가 아닌 수로 변경
        j = 2
        while i * j <= n:
            is_prime[i * j] = False
            j += 1
```

<br>

### 팩토리얼

- 일반적으로 사용하는 간단한 구현

```python
# 1. math 모듈 활용
import math

# 2. 반복문 활용
def factorial_for(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

# 3. 재귀 활용
def factorial_recursive(n):
    return n * factorial_recursive(n-1) if n > 1 else 1
```
```python
>>> math.factorial(5)
120
>>> factorial_for(5)
120
>>> factorial_recursive(5)
120
```

- Memoization을 사용해 효율성을 극대화

```python
# 1. 전역 공간에 캐쉬 생성
cache = {}

def factorial_recursive(n):
    global cache

    if n in cache:
        return cache[n]
    elif n <= 1:
        return 1
    else:
        cache[n] = n * factorial_recursive(n-1)
	    return cache[n]

# 2. 개선한 캐쉬 활용법
def in_cache(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]
    return wrapper

@in_cache
def factorial_recursive(n):
    return n * factorial_recursive(n-1) if n > 1 else 1
```
 > - 캐시가 전역에 선언하는 것보다 in_cache 내의 이름공간을 쓰는 것이 더 안전<br>
 > - 캐시에 값을 확인하는 코드와 실제 계산하는 코드가 분리되어 재사용성이 강화<br>

- 다른 함수 사용

```python
# reduce 함수 사용
from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n+1))

# eval 함수를 사용한 Meta programming
def factorial_meta(n):
    if not n:
        return 1
    return eval('*'.join(str(i) for i in range(1, n+1)))
```
```python
>>> factorial_reduce(5)
120
>>> factorial_meta(5)
120
```