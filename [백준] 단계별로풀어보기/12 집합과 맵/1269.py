import sys
input = sys.stdin.readline

# 문제정보 입력받기
N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# 결과 출력하기
print(len(A.symmetric_difference(B)))  # 대칭 차집합을 계산해주는 함수

'''
# 교집합 수 파악 후 결과 계산
count = 0
for data in A:
    if data in B:
        count += 1

print(N + M - 2 * count)
'''