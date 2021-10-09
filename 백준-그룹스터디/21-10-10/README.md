## 2021 / 10 / 10 (일) 10:00  >> (변경) 2021 / 10 / 11 (월) 13:00

|문제 번호|문제 제목|문제 풀이|문제 분류|
|:---:|---|:---:|---|
|[16985](https://www.acmicpc.net/problem/16985)|Maaaaaaaaaze|[python](16985.py)|구현, 그래프 이론, 그래프 탐색, 브루트포스 알고리즘, 너비 우선 탐색|
|[3665](https://www.acmicpc.net/problem/3665)|최종 순위|[python](3665.py)|그래프 이론, 위상 정렬|
|[1561](https://www.acmicpc.net/problem/1561)|놀이 공원|[python](1561.py)|이분 탐색, 매개 변수 탐색|
|[2042](https://www.acmicpc.net/problem/2042)|구간 합 구하기|[python](2042.py)|자료 구조, 세그먼트 트리|
|[5427](https://www.acmicpc.net/problem/5427)|불|[python](5427.py)|구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색|

<br>

---

### Maaaaaaaaaze



<br>

### 최종 순위



<br>

### 놀이 공원



<br>

### 구간 합 구하기



<br>

### 불

#### queue.Queue() <-> deque()

```python
from queue import Queue
while not Queue.empty():

from collections import deque
while deque:
```

Queue를 만들어서 Queue에 원소가 없을 때까지 원소를 꺼내는 동작을 수행할 때 queue.Queue()를 통해 생성한 큐는 비어있는지를 method를 이용해 확인한 후 not 처리를 해주어야하지만, deque()를 이용할 경우 큐를 비어있는지 확인하는 boolean으로 사용할 수 있었다.
이러한 차이가 동작 시간의 차이를 유발하는지 deque로 변경했을 때 시간 초과가 사라졌다.

#### 놓친 반례

시작 위치가 탈출구인 경우를 고려하지 못해 반례를 찾는데 굉장히 오래 걸렸다.

#### 시간 단축

이미 사람이 지나간 길을 불이 따라갈 필요가 없었다. 이것으로 인해 pypy3로만 통과되던 코드가 python3로도 통과할 수 있게 되었다.

<br>