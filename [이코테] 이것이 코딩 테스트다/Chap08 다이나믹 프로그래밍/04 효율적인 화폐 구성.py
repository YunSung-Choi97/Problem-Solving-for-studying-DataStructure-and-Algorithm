INF = 10001

n, m = map(int, input().split())  # 화폐 개수, 목표 금액

array = set()  # 화폐의 가치 (중복 제거)
for _ in range(n):
    array.add(int(input()))
array = list(array)

dp = [0] + [INF] * m
for i in range(1, m + 1):
    for j in range(n):
        # 만들지 못하는 경우
        if i - array[j] < 0 or dp[i - array[j]] == INF:
            continue
        # i원을 만들기 위한 최소한의 화폐 개수 저장
        dp[i] = min(dp[i], dp[i - array[j]] + 1)

# 결과 출력
if dp[m] == INF:
    print(-1)
else:
    print(dp[m])

''' 입력 예시 1
2 15
2
3
'''
''' 출력 예시 1
5
'''

''' 입력 예시 2
3 4
3
5
7
'''
''' 출력 예시 2
-1
'''