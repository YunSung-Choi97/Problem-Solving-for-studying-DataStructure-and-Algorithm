import sys
input = sys.stdin.readline

# 듣도 못한 사람의 이름 저장
N, M = map(int, input().split())
no_hear = set()
for _ in range(N):
    no_hear.add(input().rstrip())

# 결과를 저장할 변수와 리스트
answer = 0
results = list()

# 보도 못한 사람의 이름을 받으며 듣도 보도 못한 사람 확인
for _ in range(M):
    no_see = input().rstrip()
    if no_see in no_hear:
        answer += 1
        results.append(no_see)

# 정답 출력
print(answer)
results.sort()
for result in results:
    print(result)