T = int(input())  # T : 테이스 케이스의 개수를 입력받음

for i in range(T):  # T번 반복
    A, B = map(int, input().split())  # A, B : 덧셈 연산을 수행할 두 정수를 입력받음
    print(A+B)