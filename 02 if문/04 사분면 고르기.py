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