N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))

result = 0
# 큰 가치를 갖는 동전을 최대한 많은 개수가 되도록 우선계산해줌.
for i in range(1, N+1):
    if K >= coins[N-i]:
        result += K // coins[N-i]
        K %= coins[N-i]
    elif K == 0:
        break

print(result)