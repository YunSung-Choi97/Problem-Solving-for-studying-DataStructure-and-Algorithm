import sys
input = sys.stdin.readline

# 문제정보 입력받기
N = int(input())
A = list(map(int, input().split()))

# 가장 긴 증가하는 부분 수열의 길이를 저장
LIS_length = [1] * N
for i in range(1, N):
    for j in range(i - 1, -1, -1):
        if A[j] < A[i] and LIS_length[j] + 1 > LIS_length[i]:
            LIS_length[i] = LIS_length[j] + 1

# 결과 출력
print(max(LIS_length))