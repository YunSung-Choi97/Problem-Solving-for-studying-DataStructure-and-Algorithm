import sys
input = sys.stdin.readline

# 문제정보 입력받기
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 누적 합의 나머지 저장
prefix_sum = 0
remainder = [0] * M
for i in range(N):
    prefix_sum += A[i]
    remainder[prefix_sum % M] += 1

# 누적 합의 나머지가 같은 수들 중 서로 다른 2개를 뽑으면 나머지가 0 (nC2)
result = 0
for r in remainder:
    result += r * (r - 1) // 2
result += remainder[0]  # 나머지가 0인 경우 자기 자신만으로도 나머지가 0

# 결과 출력
print(result)