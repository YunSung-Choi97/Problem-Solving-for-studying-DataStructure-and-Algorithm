## 2021 / 10 / 03 (일) 10:00

|문제 번호|문제 제목|문제 풀이|문제 분류|
|:---:|---|:---:|---|
|[3954](https://www.acmicpc.net/problem/3954)|Brainf**k 인터프리터|[python](3954.py)|구현, 자료 구조, 스택|
|[15961](https://www.acmicpc.net/problem/15961)|회전 초밥|[python](15961.py)|두 포인터, 슬라이딩 윈도우|
|[2116](https://www.acmicpc.net/problem/2116)|주사위 쌓기|[python](2116.py)|구현, 브루트포스 알고리즘|
|[2169](https://www.acmicpc.net/problem/2169)|로봇 조종하기|[python](2169.py)|다이나믹 프로그래밍|
|[3109](https://www.acmicpc.net/problem/3109)|빵집|[python](3109-2.py)|그래프 이론, 그리디 알고리즘, 그래프 탐색, 깊이 우선 탐색|

<br>

---

### Brainf**k 인터프리터

문제를 정확히 이해하기 어려웠고, 무한루프인 경우 루프 구간을 찾는 것이 굉장히 어려웠던 문제

<br>

### 회전 초밥

- 둘 중 큰 값으로 할당 연산시간 비교

A(정답을 저장할 변수)와 B(변하는 변수)를 반복적으로 크기 비교하여 더 큰 값을 A(정답을 저장할 변수)에 할당하는 부분이 있다. 이 부분에서 max(A, B)를 이용하는 것보다 if문을 이용해 대소관계를 확인하여 값을 변화시키는 것이 더 빠른 모습을 보이는 것을 확인할 수 있었다.

코드 중 일부분
```python
# 쿠폰 메뉴 확인
if eat[coupon] == 0:
    # answer = max(answer, menu_count + 1)  # 변경 전 코드
    if answer < menu_count + 1:
        answer = menu_count + 1
else:
    # answer = max(answer, menu_count)  # 변경 전 코드
    if answer < menu_count:
        answer = menu_count
```

<br>

### 주사위 쌓기

구현

<br>

### 로봇 조종하기

DP table을 3개 만들어주는 아이디어가 중요!<br>
DP_left와 DP_right으로 DP를 완성해나가는 구조

<br>

### 빵집

DFS 이용

<br>