# 04 while문

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

<br>

---

# *Source Code*

## 01 A + B (5)

```python
while True:  # 무한 반복
    A, B = map(int, input().split())  # 
    if A == 0 & B == 0:  # 무한 루프를 빠져나오는 조건
        break
    print(A+B)
```

## 02 A + B (4)

```python
while True:  # 무한 반복
    
    # 무한 루프의 종료조건이 문제에 제시되었지 않았기 때문에, 에러가 발생하기 전까지는 프로그램이 동작하도록 해주었다.
    # try, except : 에러가 발생할 경우에 대한 처리
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
```

## 03 더하기 사이클

```python
initial_num = int(input())  # initial_num : 사용자로부터 입력받을 N.

count = 1  # count : 결과로 출력할 사이클 수
while True:  # 무한 반복
    
    # num을 초기화시켜준다
    if count == 1:
        num = initial_num
    else:
        num = new_num
    num10 = num // 10  # num10 : num의 10의 자리 수
    num1 = num % 10  # num1 : num의 1의 자리 수
    new_num = 10 * num1 + (num10 + num1) % 10  # new_num : num으로 만든 새로운 수
    if initial_num == new_num:  # 반복문 종료 조건. 입력받은 수가 새로운 수와 같아질 때
        print(count)
        break
    count += 1  # 사이클 수는 반복문이 수행될때마다 1씩 증가
```