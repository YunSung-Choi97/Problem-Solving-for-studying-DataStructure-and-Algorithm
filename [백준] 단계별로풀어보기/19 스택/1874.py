import sys
input = sys.stdin.readline

n = int(input())  # 입력정보 n 저장

having_sequence = [i for i in range(n, 0, -1)]  # 가진 수열 (n, n-1, n-2, ..., 3, 2, 1)
making_sequence = list()  # 만들 수열
for _ in range(n):
    making_sequence.append(int(input()))

stack = list()  # 만들 수열을 만드는 과정에서 사용할 스택
result = list()  # push와 pop 로그 기록 저장
can_make = True  # 만들 수 있는 수열인지 확인
for i in range(n):
    while len(having_sequence) != 0 and having_sequence[-1] <= making_sequence[i]:
        stack.append(having_sequence.pop())
        result.append('+')
    if stack[-1] == making_sequence[i]:
        stack.pop()
        result.append('-')
    else:
        can_make = False
        break

# 결과 출력
if can_make:
    for char in result:
        print(char)
else:
    print('NO')