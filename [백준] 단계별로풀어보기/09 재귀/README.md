# 09 재귀

|문제 번호|문제 제목|문제 풀이|
|:---:|---|:---:|
[10872](https://www.acmicpc.net/problem/10872)|팩토리얼|[python](10872.py)
[10870](https://www.acmicpc.net/problem/10870)|피보나치 수 5|[python](10870.py)
[17478](https://www.acmicpc.net/problem/17478)|재귀함수가 뭔가요?|[python](17478.py)
[2447](https://www.acmicpc.net/problem/2447)|별 찍기 - 10|[python](2447.py)
[11729](https://www.acmicpc.net/problem/11729)|하노이 탑 이동 순서|[python](11729.py)

---

## Summary

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

참고자료 : <https://shoark7.github.io/programming/algorithm/several-ways-to-solve-factorial-in-python>

<br>

### 문자열

- .join()

> '구분자'.join(리스트) 형태로 사용하며, 매개 변수로 전달받은 리스트의 요소와 요소 사이에 구분자를 넣어 하나의 문자열로 합쳐 반환한다.