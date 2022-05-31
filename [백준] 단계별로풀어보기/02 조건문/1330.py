A, B = map(int, input().split())  # A, B : 정수 A, B를 입력받음

# 조건문을 통해 두 수의 대소관계를 확인
if A < B:
    print("<")
elif A > B:
    print(">")
else:
    print("==")