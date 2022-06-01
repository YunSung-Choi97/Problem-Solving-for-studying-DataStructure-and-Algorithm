# 08 기본 수학 2

|문제 번호|문제 제목|문제 풀이|
|:---:|---|:---:|
[1978](https://www.acmicpc.net/problem/1978)|소수 찾기|[python](1978.py)
[2581](https://www.acmicpc.net/problem/2581)|소수|[python](2581.py)
[11653](https://www.acmicpc.net/problem/11653)|소인수분해|[python](11653.py)
[1929](https://www.acmicpc.net/problem/1929)|소수 구하기|[python](1929.py)
[4948](https://www.acmicpc.net/problem/4948)|베르트랑 공준|[python](4948.py)
[9020](https://www.acmicpc.net/problem/9020)|골드바흐의 추측|[python](9020.py)

---

## Summary

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