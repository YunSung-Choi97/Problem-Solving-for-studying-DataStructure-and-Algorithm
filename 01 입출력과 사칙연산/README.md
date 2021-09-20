# 01 입출력과 사칙연산

|번호|문제 제목|나의 풀이|
|---|---|---|
[2557](https://www.acmicpc.net/problem/2557)|Hello World|[code](01_2557.py)
[10718](https://www.acmicpc.net/problem/10718)|We love kriii|[code](02_10718.py)
[10171](https://www.acmicpc.net/problem/10171)|고양이|[code](03_10171.py)
[10172](https://www.acmicpc.net/problem/10172)|개|[code](04_10172.py)
[1000](https://www.acmicpc.net/problem/1000)|A+B|[code](05_1000.py)
[1001](https://www.acmicpc.net/problem/1001)|A-B|[code](06_1001.py)
[10998](https://www.acmicpc.net/problem/10998)|AxB|[code](07_10998.py)
[1008](https://www.acmicpc.net/problem/1008)|A/B|[code](08_1008.py)
[10869](https://www.acmicpc.net/problem/10869)|사칙연산|[code](09_10869.py)
[10430](https://www.acmicpc.net/problem/10430)|나머지|[code](10_10430.py)
[2588](https://www.acmicpc.net/problem/2588)|곱셈|[code](11_2588.py)

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