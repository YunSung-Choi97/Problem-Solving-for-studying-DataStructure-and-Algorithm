# 05 1차원 배열

|번호|문제 제목|나의 풀이|
|---|---|---|
[10818](https://www.acmicpc.net/problem/10818)|최소, 최대|[code](01_10818.py)
[2562](https://www.acmicpc.net/problem/2562)|최댓값|[code](02_2562.py)
[2577](https://www.acmicpc.net/problem/2577)|숫자의 개수|[code](03_2577.py)
[3052](https://www.acmicpc.net/problem/3052)|나머지|[code](04_3052.py)
[1546](https://www.acmicpc.net/problem/1546)|평균|[code](05_1546.py)
[8958](https://www.acmicpc.net/problem/8958)|OX퀴즈|[code](06_8958.py)
[4344](https://www.acmicpc.net/problem/4344)|평균은 넘겠지|[code](07_4344.py)

---

## Summary

### 함수

- len()

> 순서열의 길이를 반환하는 함수

<br>

### 리스트

- .append()

> 입력 파라미터를 리스트의 가장 마지막에 추가하는 함수

- .sort() / sorted()

> 리스트의 요소를 기본적으로 오름차순으로 정렬해준다.

> .sort(reverse=True) : 이와 같이 reverse를 이용하면 내림차순으로 정렬된다.<br>
 .sort(key=lambda x:x[1]) : key와 매개변수를 이용하여 정렬하기전 정렬 기준이 되는 key값을 지정할 수 있다. 여기에 함수를 사용하거나, lambda를 통해 간단히 함수를 구현하여 정렬 기준을 설정해줄 수 있다.<br>
 <=> sorted() : 기본적으로 오름차순으로 정렬해주는 동일한 역할을 하는 함수이다. .sort()는 리스트에 대하여 본인을 정렬된 리스트값으로 바꿔주는 함수이고, sorted()는 파라미터로 리스트 뿐만아니라 다양한 순서열을 받을 수 있고 정렬된 리스트를 반환한다.
 
- .index() / find()

> 리스트 내에서 입력 파라미터로 받은 요소의 인덱스 값을 반환하는 함수

> .index(value1, start, end) : 이와 같이 리스트 내에서 찾고자하는 val1을 입력해주고, 범위를 정하고 싶다면 start와 end를 사용해줄 수 있다. val1이 리스트 내에 여러개 존재한다면 첫번째 인덱스를 반환하기때문에, index()에서 start에 index(value1)+1을 넣어 두번째 위치를 찾을 수 있다.<br>
 <=> .find() : 동일하게 리스트 내에서 찾고자하는 값의 인덱스를 반환해주는 함수<br>
 리스트 내에 찾는 값이 없을 경우 index()는 ValueError가 발생하고, find()는 -1을 반환한다.

<br>

### 수학

- max() / min()

> 입력 파라미터 내에서 최댓값/최솟값을 반환하는 함수

- sum()

> 입력 파라미터들의 합산값을 반환하는 함수

