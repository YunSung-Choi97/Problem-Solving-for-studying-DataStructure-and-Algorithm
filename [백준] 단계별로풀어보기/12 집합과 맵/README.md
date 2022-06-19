# 12 집합과 맵

|문제 번호|문제 제목|문제 풀이|
|:---:|---|:---:|
[10815](https://www.acmicpc.net/problem/10815)|숫자 카드|[python](10815.py)
[14425](https://www.acmicpc.net/problem/14425)|문자열 집합|[python](14425.py)
[1620](https://www.acmicpc.net/problem/1620)|나는야 포켓몬 마스터 이다솜|[python](1620.py)
[10816](https://www.acmicpc.net/problem/10816)|숫자 카드 2|[python](10816.py)
[1764](https://www.acmicpc.net/problem/1764)|듣보잡|[python](1764.py)
[1269](https://www.acmicpc.net/problem/1269)|대칭 차집합|[python](1269.py)
[11478](https://www.acmicpc.net/problem/11478)|서로 다른 부분 문자열의 개수|[python](11478.py)

---

## Summary

### 집합

- .intersection(), .union(), .difference(), .symmetric_difference()

 > 집합간에 교집합, 합집합, 차집합, 대칭차집합을 계산해준다. 이 외에도 서로소, 포함관계를 확인하는 매소드도 있다.

```python
A = set([1, 2, 3, 4])
B = set([3, 4, 5, 6])
```
```
>>> A.intersection(B)
{3, 4}
>>> A.union(B)
{1, 2, 3, 4, 5, 6}
>>> A.difference(B)
{1, 2}
>>> A.symmetric_difference(B)
{1, 2, 5, 6}
```