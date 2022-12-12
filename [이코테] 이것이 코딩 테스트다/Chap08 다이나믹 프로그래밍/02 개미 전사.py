n = int(input())  # 식량창고의 개수
array = list(map(int, input().split()))  # 식량창고에 저장된 식량의 개수

dp = [0] * n  # 계산 결과 저장 리스트
dp[0] = array[0]
dp[1] = max(array[0], array[1])
for i in range(2, n):
    dp[i] = max(dp[i - 2] + array[i], dp[i - 1])

print(dp[n - 1])  # 결과 출력

''' 입력 예시 1
4
1 3 1 5
'''
''' 출력 예시 1
8
'''