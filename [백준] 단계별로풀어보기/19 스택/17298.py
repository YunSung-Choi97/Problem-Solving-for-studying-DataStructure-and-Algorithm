import sys
input = sys.stdin.readline

# 문제정보 입력받기
N = int(input())
A = list(map(int, input().split()))

answer = [-1] * N  # 결과 저장
stack = []
stack.append(0)  # 오큰수를 찾아야 할 idx값 저장
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

# 결과 출력
print(*answer)