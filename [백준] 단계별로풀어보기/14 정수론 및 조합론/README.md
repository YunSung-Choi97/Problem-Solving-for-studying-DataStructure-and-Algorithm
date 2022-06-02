# 14 정수론 및 조합론

|문제 번호|문제 제목|문제 풀이|
|:---:|---|:---:|
[5086](https://www.acmicpc.net/problem/5086)|배수와 약수|[python](5086.py)
[1037](https://www.acmicpc.net/problem/1037)|약수|[python](1037.py)
[2609](https://www.acmicpc.net/problem/2609)|최대공약수와 최소공배수|[python](2609.py)
[1934](https://www.acmicpc.net/problem/1934)|최소공배수|[python](1934.py)
[2981](https://www.acmicpc.net/problem/2981)|검문|[python](2981.py)
[3036](https://www.acmicpc.net/problem/3036)|링|[python](3036.py)
[11050](https://www.acmicpc.net/problem/11050)|이항 계수 1|[python](11050.py)
[11051](https://www.acmicpc.net/problem/11051)|이항 계수 2|[python](11051.py)
[1010](https://www.acmicpc.net/problem/1010)|다리 놓기|[python](1010.py)
[9375](https://www.acmicpc.net/problem/9375)|패션왕 신해빈|[python](9375.py)
[1676](https://www.acmicpc.net/problem/1676)|팩토리얼 0의 개수|[python](1676.py)
[2004](https://www.acmicpc.net/problem/2004)|조합 0의 개수|[python](2004.py)

---

## Summary

### 알고리즘

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