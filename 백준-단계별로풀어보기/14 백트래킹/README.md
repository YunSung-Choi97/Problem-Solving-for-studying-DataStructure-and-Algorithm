# 14 백트래킹

|번호|문제 제목|나의 풀이|Memo|
|---|---|---|---|
[15649](https://www.acmicpc.net/problem/15649)|N과 M (1)|[code](01_15649.py)|순열
[15650](https://www.acmicpc.net/problem/15650)|N과 M (2)|[code](02_15650.py)|조합
[15651](https://www.acmicpc.net/problem/15651)|N과 M (3)|[code](03_15651.py)|중복 순열
[15652](https://www.acmicpc.net/problem/15652)|N과 M (4)|[code](04_15652.py)|중복 조합
[9663](https://www.acmicpc.net/problem/9663)|N-Queen|[code](05_9663.py)|
[2580](https://www.acmicpc.net/problem/2580)|스도쿠|[code](06_2580.py)|
[14888](https://www.acmicpc.net/problem/14888)|연산자 끼워넣기|[code](07_14888.py)|
[14889](https://www.acmicpc.net/problem/14889)|스타트와 링크|[code](08_14889.py)|

---

## Summary

### 기타

- global

> 지역변수를 전역변수로 사용하고자 할때 global (변수명)과 같이 작성해주면 된다.

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