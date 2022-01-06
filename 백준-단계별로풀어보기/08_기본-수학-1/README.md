# 08 기본 수학 1

|번호|문제 제목|나의 풀이|
|---|---|---|
[1712](https://www.acmicpc.net/problem/1712)|손익분기점|[code](01_1712.py)
[2292](https://www.acmicpc.net/problem/2292)|벌집|[code](02_2292.py)
[1193](https://www.acmicpc.net/problem/1193)|분수찾기|[code](03_1193.py)
[2869](https://www.acmicpc.net/problem/2869)|달팽이는 올라가고 싶다|[code](04_2869.py)
[10250](https://www.acmicpc.net/problem/10250)|ACM 호텔|[code](05_10250.py)
[2775](https://www.acmicpc.net/problem/2775)|부녀회장이 될테야|[code](06_2775.py)
[2839](https://www.acmicpc.net/problem/2839)|설탕 배달|[code](07_2839.py)
[10757](https://www.acmicpc.net/problem/10757)|큰 수 A+B|[code](08_10757.py)
[1011](https://www.acmicpc.net/problem/1011)|Fly me to the Alpha Centauri|[code](09_1011.py)

---

## Summary

### 수학

- round()

> 내장 함수로 입력 파라미터의 반올림 값을 반환하는 함수<br>
 두번째 값으로 몇번째 자리까지 나타낼지 정해줄 수 있다.

```python
>>> round(3.141592)
3

>>> round(3.141592, 2)
3.14

>>> round(31.41592, -1)
30.0
```

- math.ceil()

> math 라이브러리를 호출한 뒤 사용가능하며, 입력 파라미터의 올림 값을 반환하는 함수

- math.floor()

> math 라이브러리를 호출한 뒤 사용가능하며, 입력 파라미터의 내림 값을 반환하는 함수

- math.trunc()

> math 라이브러리를 호출한 뒤 사용가능하며, 입력 파라미터의 0을 향한 내림 값을 반환하는 함수. 즉, 양수에서는 내림을 수행하고 음수에서는 올림을 수행한다.