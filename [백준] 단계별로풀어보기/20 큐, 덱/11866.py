from collections import deque

# 문제정보 입력받기
N, K = map(int, input().split())

# Queue에 1 ~ N 저장
queue = deque()
for i in range(1, N + 1):
    queue.append(i)

count = 0  # K번째 사람을 찾기 위한 사람 수 확인변수
result = list()  # 결과를 저장할 리스트
# 요세푸스 순열 구하기
while queue:
    if count == K - 1:
        result.append(queue.popleft())
        count = 0
    else:
        queue.append(queue.popleft())
        count += 1

# 결과 출력
print('<', end='')
for i in range(N - 1):
    print(result[i], end=', ')
print('{}>'.format(result[-1]))