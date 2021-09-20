# 04 while문

|번호|문제 제목|나의 풀이|
|---|---|---|
[10952](https://www.acmicpc.net/problem/10952)|A+B - 5|[code](01_10952.py)
[10951](https://www.acmicpc.net/problem/10951)|A+B - 4|[code](02_10951.py)
[1110](https://www.acmicpc.net/problem/1110)|더하기 사이클|[code](03_1110.py)

---

## Summary

### **반복문**

- while문

> while (condition):<br>
&nbsp;&nbsp;&nbsp;&nbsp;(code block)<br>

> while문은 while 바로 다음 작성되는 조건에 대하여 조건이 참일 경우 아래 코드블록을 수행하게 된다. 따라서, 어떤 동작을 조건에 맞는 상황에서만 반복수행하고 싶을 때 사용하게 된다.<br>
 조건을 항상 참으로 만들어 무한 루프가 되지 않도록 주의해야한다.

- continue, break

> continue/break를 이용하면 반복문을 조금 더 효율적으로 사용할 수 있다.<br>
 반복문 내에서 continue를 만나게 되면 아래의 코드를 통과하고 반복문의 다음 차례로 넘어가게 된다. break를 만나게 되면 아래의 코드를 통과하고 반복문을 끝내게 된다.<br>
 따라서, continue는 주로 특정 상황에 대하여 아래의 동작을 수행하고 싶지않거나 확인할 필요가 없는 경우에 많이 사용한다. break는 주로 무한 루프를 끝내거나 수행하고 싶은 동작을 모두 했을 때 끝내고 넘어가기 위한 방법으로 많이 사용된다.

<br>

### **에러와 예외 처리**

- try, except, raise, else, finally

> try:<br>
 &nbsp;&nbsp;&nbsp;&nbsp;(code block)<br>
 except:<br>
 &nbsp;&nbsp;&nbsp;&nbsp;(code block)<br>

> 에러가 발생할 가능성이 있는 코드를 try의 코드 블록안에 넣어줌으로서, 에러가 발생했을 때 에러표시와 프로그램 종료가 아닌 원하는 수행동작을 except의 코드 블록에 넣어 에러에 대한 처리가 가능하다.<br>
 추가로, raise를 이용하면 원하는 에러를 발생시킬수 있다. 그리고 except 아래에 else/finally구문을 이용하여 에러가 발생하지 않은 경우/예외 발생 여부와 관계없이 모든 경우에 대하여 수행할 동작을 작성해줄 수 있다.