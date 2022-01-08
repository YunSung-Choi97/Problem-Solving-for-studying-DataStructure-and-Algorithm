## 2021 / 10 / 17 (일) 10:00

|문제 번호|문제 제목|문제 풀이|문제 분류|
|:---:|---|:---:|---|
|[21610](https://www.acmicpc.net/problem/21610)|마법사 상어와 비바라기|[python](21610.py)|구현, 시뮬레이션|
|[17779](https://www.acmicpc.net/problem/17779)|게리맨더링 2|[python](17779.py)|구현, 브루트포스 알고리즘, 시뮬레이션|
|[20061](https://www.acmicpc.net/problem/20061)|모노미노도미노 2|[python](20061.py)|구현, 시뮬레이션|
|[2637](https://www.acmicpc.net/problem/2637)|장난감 조립|[python](2637.py)|다이나믹 프로그래밍, 그래프 이론, 위상 정렬|
|[3114](https://www.acmicpc.net/problem/3114)|사과와 바나나|[python](3114.py)|다이나믹 프로그래밍, 누적 합|

<br>

---

### Maaaaaaaaaze

완전탐색, BFS

<br>

### 최종 순위

위상 정렬
```python
# 위상정렬
def topology_sort():
    result = []
    queue = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
    
    # 큐가 빌 때까지
    while queue:
        now = queue.popleft()
        result.append(now)

        # 연결된 노드들 진입차수 -1
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    
    return result
```

<br>

### 놀이 공원

이분 탐색

<br>

### 구간 합 구하기

세그먼트 트리에 대한 개념이 부족하여 dict()를 이용하여 pypy3로 해결.

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