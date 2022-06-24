import sys
input = sys.stdin.readline

# 문제정보 입력받기
N = int(input())
S = list(map(int, input().split()))

# 왼쪽부터 가장 긴 증가하는 부분 수열의 길이를 저장
LIS_length_left = [1] * N
for i in range(1, N):
    for j in range(i - 1, -1, -1):
        if S[j] < S[i] and LIS_length_left[j] + 1 > LIS_length_left[i]:
            LIS_length_left[i] = LIS_length_left[j] + 1

# 오른쪽부터 가장 긴 증가하는 부분 수열의 길이를 저장
LIS_length_right = [1] * N
for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if S[i] > S[j] and LIS_length_right[i] < LIS_length_right[j] + 1:
            LIS_length_right[i] = LIS_length_right[j] + 1

# 가장 긴 바이토닉 부분 수열의 길이 저장
result = 1
for i in range(N):
    if result < LIS_length_left[i] + LIS_length_right[i] - 1:
        result = LIS_length_left[i] + LIS_length_right[i] - 1

# 결과 출력
print(result)