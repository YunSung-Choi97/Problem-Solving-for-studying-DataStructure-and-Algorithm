# 01 입출력과 사칙연산

|번호|문제 제목|나의 풀이|
|---|---|---|
[2557](https://www.acmicpc.net/problem/2557)|Hello World|[code](2557.py)
[10718](https://www.acmicpc.net/problem/10718)|We love kriii|[code](10718.py)
[10171](https://www.acmicpc.net/problem/10171)|고양이|[code](10171.py)
[25083](https://www.acmicpc.net/problem/25083)|새싹|[code](25083.py)
[1000](https://www.acmicpc.net/problem/1000)|A+B|[code](1000.py)
[1001](https://www.acmicpc.net/problem/1001)|A-B|[code](1001.py)
[10998](https://www.acmicpc.net/problem/10998)|AxB|[code](10998.py)
[1008](https://www.acmicpc.net/problem/1008)|A/B|[code](1008.py)
[10869](https://www.acmicpc.net/problem/10869)|사칙연산|[code](10869.py)
[10926](https://www.acmicpc.net/problem/10926)|??!|[code](10926.py)
[18108](https://www.acmicpc.net/problem/18108)|사칙연산|[code](18108.py)
[10430](https://www.acmicpc.net/problem/10430)|나머지|[code](10430.py)
[2588](https://www.acmicpc.net/problem/2588)|곱셈|[code](2588.py)

---

## Summary

### **함수**

- print()

> 입력받은 인자를 화면에 출력해 주는 함수<br>
 ','로 구분하여 여러 파라미터를 동시에 출력할 수 있다.<br>
 sep : print(value1, value2, sep=value3)와 같이 사용하여 val1과 val2를 val3로 구분하여 출력할 수 있다. 기본값은 ' '(공백)이다.<br>
 end : print(value1, end=value2)와 같이 사용하면 val1을 출력한 후(모든 입력 인자를 출력한 후) value2을 출력한다. 기본값은 '\n'(줄바꿈)이다.<br>

- input()

> 사용자로부터 입력받은 값을 리턴하는 함수<br>
 input(value1)와 같이 사용하면 입력받기 전 val1을 화면에 출력하게 된다.<br>

- map()

> 일반적으로 map(함수, 데이터)와 같이 입력 받는다.<br>
 입력받은 데이터에 앞의 함수를 적용하여 하나씩 리턴해준다.<br>

<br>

### **문자열**

- .split()

> 구분자를 기준으로 문자열을 나누어 리스트형으로 반환해준다.<br>
 기본값으로 ' '(공백), '\t'(tab), '\n'(줄바꿈)을 기준으로 문자열을 나눠 리스트 형태로 리턴해준다.<br>
 .split(value1)과 같이 사용하면 val1이 구분자가 된다.<br>