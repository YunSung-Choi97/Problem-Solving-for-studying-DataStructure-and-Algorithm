# 15 백트래킹

|문제 번호|문제 제목|문제 풀이|
|:---:|---|:---:|
[15649](https://www.acmicpc.net/problem/15649)|N과 M (1)|[python](15649.py)
[15650](https://www.acmicpc.net/problem/15650)|N과 M (2)|[python](15650.py)
[15651](https://www.acmicpc.net/problem/15651)|N과 M (3)|[python](15651.py)
[15652](https://www.acmicpc.net/problem/15652)|N과 M (4)|[python](15652.py)
[9663](https://www.acmicpc.net/problem/9663)|N-Queen|[python](9663.py)
[2580](https://www.acmicpc.net/problem/2580)|스도쿠|[python](2580.py)
[14888](https://www.acmicpc.net/problem/14888)|연산자 끼워넣기|[python](14888.py)
[14889](https://www.acmicpc.net/problem/14889)|스타트와 링크|[python](14889.py)

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