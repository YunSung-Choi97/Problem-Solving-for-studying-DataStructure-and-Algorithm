## Note

이 부분은 학습하며 알게된 내용, 편리하게 사용될 것 같은 내용들을 주관적으로 정리한 부분으로, 계속해서 추가와 숙지된 내용에 대한 삭제가 이루어질 것이다.

### 수 자료형  ex) 정수, 실수

#### 지수 표현 방식

e 또는 E 를 이용한 지수 표현이 가능하다. 이때 값은 실수형으로 만들어진다.<br>
최단 경로 알고리즘에서 도달할 수 없는 노드에 대하여 최단 거리를 무한(INF)으로 설정하곤 한다. ex) INF = 1e9
```python
a = 1e9     # 1,000,000,000.0
b = 75.25e1 # 752.5
c = 3594e-3 # 3.954
```

#### 반올림

round() 함수를 이용해 반올림 계산한다.
```python
round(123.456, 2)  # 소수점 2자리까지 표현(3째자리에서 반올림) : 123.46
```

### 순서열 자료형  ex) 리스트, 문자열, 튜플, 사전, 집합

#### 리스트 초기화

```python
# 빈 리스트
array = []
array = list()

# 크기가 N, 모든 값이 0인 1차원 리스트
N = 10
array = [0] * N

# 리스트 컴프리헨션
array = [0 for i in range(N)]  # 크기가 N, 모든 값이 0인 리스트
array = [i for i in range(1, 11)]  # 1 ~ 10까지의 수를 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]  # 0 ~ 19까지의 수 중 홀수만 포함하는 리스트
array = [i*i for i in range(1, 10)]  # 1 ~ 9의 제곱값을 포함하는 리스트

array = [[0] * M for _ in range(N)]  # 모든 값이 0인 N * M 크기의 2차원 리스트
```

#### 특정 값 가지는 원소 모두 제거
```python
a = [1, 2, 3, 4, 4, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]  # [1, 2, 4, 4]
```

#### 튜플을 사용하면 좋은 경우

1. 서로 다른 성질의 데이터를 묶어서 관리해야 할 때
 - ex) 최단 경로 : (비용, 노드 번호)

2. 데이터의 나열을 해싱(Hashing)의 키 값으로 사용해야 할 때
 - 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있다.

3. 리스트보다 메모리를 효율적으로 사용해야할 때

#### dict와 set의 초기화 구분

1. dict는 key와 value의 쌍을 데이터로 가지고, set은 중복을 허용하지 않고, 순서가 없다.
```python
# 빈 사전자료형, 집합 자료형 생성
D = dict()
S = set()

# 초기화
D = {'name' : 'Yunsung', 'age' : 25}  # : 를 이용하여 선언
S = {'Yunsung', 25}  # : 없이 ,를 이용하여 선언
```

#### 집합 자료형

```python
data = {1, 2, 3}

data.add(4)         # 새로운 원소 추가
data.update([5, 6]) # 새로운 원소 여러개 추가
data.remove(3)      # 특정한 값을 갖는 원소 제거
```

합집합, 교집합, 차집합의 연산이 가능
```python
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

c = a | b  # 합집합 : {1, 2, 3, 4, 5, 6, 7}
c = a & b  # 교집합 : {3, 4, 5}
c = a - b  # 차집합 : {1, 2}
```


### 일반적인 상황

#### 실전에서 유용한 표준 라이브러리

1. 내장 함수 : 기본 입출력 함수부터 정렬 함수까지 기본적인 함수 제공

2. itertools : 반복되는 형태의 데이터 처리하기 위한 유용한 기능 제공. 특히 순열과 조합 라이브러리가 자주 사용
```python
from itertools import permutations  # 순열 사용
from itertools import combinations  # 조합 사용
from itertools import product       # 중복 순열
from itertools import combinations_with_replacement  # 중복 조합
```
3. heapq : 힙(Heap) 자료구조를 제공. 우선순위 큐 기능을 구현하기 위해 주로 사용

4. bisect : 이진 탐색(Binary Search) 기능을 제공

5. collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함
```python
from collections import Counter

counter = Counter['red', 'blue', 'red', 'green', 'blue', 'blue']

print(counter['blue'])  # 3
print(counter['green']) # 1
print(dict(counter))    # {'red' : 2, 'blue' : 3, 'green' : 1}
```
6. math : 수학적 기능을 제공. ex) 팩토리얼, 제곱근, 최대공약수, 삼각함수, 파이
```python
import math

print(math.gcd(21, 14))  # 최대공약수 계산 : 7
```
#### 빠르게 입력 받기

sys 라이브러리에 정의되어 있는 sys.stdin.readline()을 이용해 더 빠르게 입력을 받을 수 있다. 이때 입력 후 엔터가 줄바꿈 기호로 입력되기때문에 rstrip()을 이용해 제거해줄 수 있다.

```python
import sys

data = sys.stdin.readline().rstrip()
```

#### 람다(lambda) 표현식

람다 표현식을 이용하면 함수를 간단하게 작성할 수 있다.

```python
print((lambda a, b: a+b)(3, 7))  # 10 출력

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
print(sorted(array, key=lambda x : x[1]))  # 2번째 값으로 오름차순 정렬 실행 : [('이순신', 32), ('홍길동', 50), ('아무개', 74)]

list1 = [1, 2, 3, 4]
list2 = [6, 7, 8, 9]
result = list(map(lambda a, b : a+b, list1, list2))  # result = [7, 9, 11, 13]
```