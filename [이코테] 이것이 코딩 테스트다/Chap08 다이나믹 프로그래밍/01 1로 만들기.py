x = int(input())
    
dp = [0] * (x + 1)  # 계산 결과 저장 리스트
for i in range(2, x + 1):
    result = []
    # 연산 1
    if i % 5 == 0:
        result.append(dp[i // 5] + 1)
    # 연산 2
    if i % 3 == 0:
        result.append(dp[i // 3] + 1)
    # 연산 3
    if i % 2 == 0:
        result.append(dp[i // 2] + 1)
    # 연산 4
    result.append(dp[i - 1] + 1)
    dp[i] = min(result)

print(dp[x])  # 결과 출력

''' 입력 예시 1
26
'''
''' 출력 예시 1
3
'''