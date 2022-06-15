import sys
input = sys.stdin.readline

# 문제정보 입력받기
N, M = map(int, input().split())
S = set()
for _ in range(N):
    S.add(input().rstrip())
data_list = list()
for _ in range(M):
    data_list.append(input().rstrip())

# 문자열 검사
answer = 0
for data in data_list:
    if data in S:
        answer += 1

# 정답 출력
print(answer)