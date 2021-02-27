# 02 if문

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

<br>

---

# *Source Code*

## 01 두 수 비교하기

```python
A, B = map(int, input().split())  # A, B : 정수 A, B를 입력받음

# 조건문을 통해 두 수의 대소관계를 확인
if A < B:
    print("<")
elif A > B:
    print(">")
else:
    print("==")
```

## 02 시험성적

```python
grade = int(input())  # grade : 시험 점수를 입력받음

# 문제의 조건에 맞게 조건을 나눠서 학점을 출력
if 90 <= grade <= 100:
    print("A")
elif 80 <= grade:  # 초기에 80 <= grade < 90: 로 작성을 했으나, 점수는 0~100점이고 위의 조건을 제외한 grade의 범위는 0~89이므로 이와 같이 작성해도 동일하다. 위의 90~100 구간도 동일하게 수정 가능하다.
    print("B")
elif 70 <= grade:
    print("C")
elif 60 <= grade:
    print("D")
else:
    print("F")
```

## 03 윤년

```python
year = int(input())  # year : 연도를 입력받음

# 문제의 조건에 맞게 조건식을 세워 윤년과 윤년이 아닌 해를 구분
if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
    print(1)
else:
    print(0)
```

## 04 사분면 고르기

```python
x = int(input())  # x : 좌표의 x값을 입력받음
y = int(input())  # y : 좌표의 y값을 입력받음

if x > 0:  # x가 양수인 경우 (1, 4 사분면)
    if y > 0:
        print(1)
    else:
        print(4)
else:  # x가 양수가 아닌 경우 (2, 3 사분면). 문제의 조건이 x, y != 0 이므로 elif로 음수인 경우가 아닌 else로 처리해도 무방하다.
    if y > 0:
        print(2)
    else:
        print(3)
```

## 05 알람 시계

```python
H, M = map(int, input().split())  # H, M : 일어날 시간을 입력받는다 (상근이가 설정해 놓은 알람시간)

# 설정할 알람 시각을 구함
if M >= 45:  # 45분보다 작은 경우에는 시간이 변하기 때문에 우선 조건으로 따져줌
    print(H, M-45)
else:
    if H == 0:  # 시간에서 1을 빼주어야 하는데 0시에서는 23로 바꿔주어야하므로 예외 처리
        print(23, M+15)
    else:
        print(H-1, M+15)
```