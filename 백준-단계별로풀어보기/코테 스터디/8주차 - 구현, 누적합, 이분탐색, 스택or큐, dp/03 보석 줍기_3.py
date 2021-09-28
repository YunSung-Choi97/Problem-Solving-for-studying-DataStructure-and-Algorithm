# 결과 : 시간 초과

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(int(input()))

results = []
for i in range(N-M+1):
    # result : (main + bonus)의 최댓값
    main = sum(data[i:i+M])  # M개의 보석 가치(i ~ i+M)
    result = main
    for j in range(i+M, len(data)):
        bonus = sum(data[i+M:j+1])  # i+M 이후의 부분합 최댓값
        if main+bonus > result:
            result = main+bonus
    results.append(result)

print(max(results))