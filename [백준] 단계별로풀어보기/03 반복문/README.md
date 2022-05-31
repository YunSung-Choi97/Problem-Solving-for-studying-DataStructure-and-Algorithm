# 03 반복문

|문제 번호|문제 제목|문제 풀이|
|:---:|---|:---:|
[2739](https://www.acmicpc.net/problem/2739)|구구단|[python](2739.py)
[10950](https://www.acmicpc.net/problem/10950)|A+B - 3|[python](10950.py)
[8393](https://www.acmicpc.net/problem/8393)|합|[python](8393.py)
[15552](https://www.acmicpc.net/problem/15552)|빠른 A+B|[python](15552.py)
[2741](https://www.acmicpc.net/problem/2741)|N 찍기|[python](2741.py)
[2742](https://www.acmicpc.net/problem/2742)|기찍 N|[python](2742.py)
[11021](https://www.acmicpc.net/problem/11021)|A+B - 7|[python](11021.py)
[11022](https://www.acmicpc.net/problem/11022)|A+B - 8|[python](11022.py)
[2438](https://www.acmicpc.net/problem/2438)|별 찍기 - 1|[python](2438.py)
[2439](https://www.acmicpc.net/problem/2439)|별 찍기 - 2|[python](2439.py)
[10871](https://www.acmicpc.net/problem/10871)|X보다 작은 수|[python](10871.py)
[10952](https://www.acmicpc.net/problem/10952)|A+B - 5|[python](10952.py)
[10951](https://www.acmicpc.net/problem/10951)|A+B - 4|[python](10951.py)
[1110](https://www.acmicpc.net/problem/1110)|더하기 사이클|[python](1110.py)

---

## Summary

### **함수**

- range()

> range(*start*, *stop*, *step*)<br>
 입력 파라미터로는 int(정수형)만 받을 수 있으며, range타입으로 반환된다.<br>
 start부터 시작하여 stop의 바로 앞까지 step의 간격으로 변화하는 정수의 배열을 나타낸다.<br>

> range(int) : 입력 파라미터가 하나인 경우 stop을 의미하고, start는 0, step은 1로 기본값이 설정되어있다.<br>
 range(int, int) : 입력 파라미터가 두개인 경우 start, stop을 의미하고, step은 1로 기본값이 설정되어있다.<br>

<br>

### **반복문**

- for문

> for 변수 in 순서열:<br>
&nbsp;&nbsp;&nbsp;&nbsp;수행할 문장들<br>

> for문의 기본 구조는 위와 같다. for와 in이 기본적으로 사용되고 가운데 변수 마지막에 순서열이 나온다. 순서열에는 일반적으로 리스트, 튜플, 문자열, range타입 등 다양한 타입이 사용된다. 이러한 경우에 순서열의 데이터를 하나씩 읽어와 변수에 할당해준 후 아래의 코드 블록을 수행하게 된다.<br>
 이 외에도 enumerate(), dict타입, 순서열 안에 순서열이 있는 형태(2차원 배열) 등과 같은 경우에, 변수 부분에 여러 변수를 넣어 한번에 여러 값을 할당받아 아래 코드 블록을 수행하도록 만들어 줄 수 있다.<br>

- while문

> while (condition):<br>
&nbsp;&nbsp;&nbsp;&nbsp;(code block)<br>

> while문은 while 바로 다음 작성되는 조건에 대하여 조건이 참일 경우 아래 코드블록을 수행하게 된다. 코드블록을 모두 수행한 뒤 다시 조건이 참인지 확인하는 과정으로 돌아간다. 따라서, 어떤 동작을 조건에 맞는 상황에서 반복수행하고 싶을 때 사용하게 된다.<br>
 조건을 항상 참으로 만들어 무한 루프가 되지 않도록 주의해야한다.

- continue, break

> continue/break를 이용하면 반복문을 조금 더 효율적으로 사용할 수 있다.<br>
 반복문 내에서 continue를 만나게 되면 아래의 코드를 통과하고 반복문의 다음 차례로 넘어가게 된다. break를 만나게 되면 아래의 코드를 통과하고 반복문을 끝내게 된다.<br>
 따라서, continue는 주로 특정 상황에 대하여 아래의 동작을 수행하고 싶지않거나 확인할 필요가 없는 경우에 많이 사용한다. break는 주로 무한 루프를 끝내거나 수행하고 싶은 동작을 모두 했을 때 끝내고 넘어가기 위한 방법으로 많이 사용된다.

<br>

### **문자열**

- .format()

> 문자열 안에 어떤 값을 삽입해 문자열을 포매팅해준다. 즉, 문자열 중간 중간에 특정 변수의 값을 넣어주기 위해 많이 사용된다.<br>
 유용하게 사용되는 몇가지 기능을 아래의 예시를 참고하여 알아보자.<br>
 1. 기본적인 포매팅<br>
 문자열 사이의 { }에 format 입력 파라미터를 순서대로 넣어준다.
 2. 인덱스를 이용한 포매팅<br>
 문자열 사이의 {index}에 index에 맞게 입력 파라미터를 넣어준다.
 3. 이름을 이용한 포매팅<br>
 문자열 사이의 {name}에 name에 맞게 입력 파라미터를 넣어준다.
 4. 문자열 정렬<br>
 {:N}을 통해 문자열의 총 자릿수를 N칸으로 하고 <, >, ^ 을 이용해 각각 왼쪽, 오른쪽, 가운데 정렬을 해줄 수 있다.
 5. 공백 채우기<br>
 문자열 정렬을 할때 : 와 정렬방향 사이에 값을 넣어 공백을 다른 값으로 채울 수 있다.
 6. 소수점 표현<br>
 {:.Nf}을 통해 소수점 아래에 대하여 자릿수를 N칸으로 설정해줄 수 있다.
 7. 종합하여 사용하기<br>
 위의 기능들은 함께 사용이 가능하다.<br>
 { } 내에 첫번째로 index/name, 두번째로 :, 세번째로 공백 채울 값, 네번째로 정렬방향, 다섯번째로 전체 자릿수, 여섯번째로 .소수점 아래 자릿수f 를 입력해주면 된다.
 8. 중괄호 { } 표현<br>
 {{}}와 같이 중괄호를 중복으로 사용하여 포매팅 역할이 아닌 중괄호로 표현이 가능하다.
 
```
>>> print("포매팅을 {} 이러한 문자열이 {}.".format("이용하면", "완성된다"))
포매팅을 이용하면 이러한 문자열이 완성된다.

>>> print("포매팅을 {1} 이러한 문자열이 {0}.".format("이용하면", "완성된다"))
포매팅을 완성된다 이러한 문자열이 이용하면.

>>> print("저는 {name}이고, {age}살입니다.".format(name = "최윤성", age = 25))
저는 최윤성이고, 25살입니다.

>>> print("문자열 정렬은 {:>10} 이렇게 사용한다.".format("Hello"))
문자열 정렬은      Hello 이렇게 사용한다.

>>> print("공백 채우기는 {:0^10} 이렇게 사용한다.".format("Hello"))
공백 채우기는 00Hello000 이렇게 사용한다.

>>> print("소수점 표현 {:.2f}".format(123.4567))
소수점 표현 123.46

>>> print("종합하여 사용하면 {number:-^10.3f} 이와 같다.".format(number = 123.45))
종합하여 사용하면 -123.450-- 이와 같다.

>>> print("{{}}를 포매팅과 {} 출력하기".format("함께"))
{}를 포매팅과 함께 출력하기
```

<br>

### **에러와 예외 처리**

- try, except, raise, else, finally

> try:<br>
 &nbsp;&nbsp;&nbsp;&nbsp;(code block)<br>
 except:<br>
 &nbsp;&nbsp;&nbsp;&nbsp;(code block)<br>

> 에러가 발생할 가능성이 있는 코드를 try의 코드 블록안에 넣어줌으로서, 에러가 발생했을 때 에러표시와 프로그램 종료가 아닌 원하는 수행동작을 except의 코드 블록에 넣어 에러에 대한 처리가 가능하다.<br>
 추가로, raise를 이용하면 원하는 에러를 발생시킬수 있다. 그리고 except 아래에 else/finally구문을 이용하여 에러가 발생하지 않은 경우/예외 발생 여부와 관계없이 모든 경우에 대하여 수행할 동작을 작성해줄 수 있다.