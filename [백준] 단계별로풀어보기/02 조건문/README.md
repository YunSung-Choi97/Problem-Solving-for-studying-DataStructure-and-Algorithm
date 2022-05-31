# 02 조건문

|문제 번호|문제 제목|문제 풀이|
|:---:|---|:---:|
[1330](https://www.acmicpc.net/problem/1330)|두 수 비교하기|[python](1330.py)
[9498](https://www.acmicpc.net/problem/9498)|시험 성적|[python](9498.py)
[2753](https://www.acmicpc.net/problem/2753)|윤년|[python](2753.py)
[14681](https://www.acmicpc.net/problem/14681)|사분면 고르기|[python](14681.py)
[2884](https://www.acmicpc.net/problem/2884)|알람 시계|[python](2884.py)
[2525](https://www.acmicpc.net/problem/2525)|오븐 시계|[python](2525.py)
[2480](https://www.acmicpc.net/problem/2480)|주사위 세개|[python](2480.py)

---

## Summary

### **조건문**

- if / elif / else구문

> if (condition):<br>
 &nbsp;&nbsp;&nbsp;&nbsp;(code block)<br>
 elif (condition):<br>
 &nbsp;&nbsp;&nbsp;&nbsp;(code block)<br>
 else:<br>
 &nbsp;&nbsp;&nbsp;&nbsp;(code block)<br>

 > 각각의 if / elif / else : if와 elif는 조건이 True일 경우 아래의 들여쓰기를 기준으로 형성된 코드블록의 코드를 수행하게 된다. else는 위에서 모든 조건이 False일 경우 마찬가지로 코드블록의 코드를 수행하게 된다.<br><br>
 elif와 else는 if 조건문 이후에만 사용할 수 있으며 필요한 경우에만 작성해주면 되고(elif는 여러개가 나타날 수 있음), 위에서부터 조건을 탐색하여 탐색한 조건이 아닌 경우에만 아래로 내려가 조건문으로 다시 들어가는 구조이고 모든 조건에 부합하지 않을 때 else문으로 들어가게 된다.<br>
 즉, ( if (A조건) .. if (B조건) ) != ( if (A조건) .. elif (B조건) )