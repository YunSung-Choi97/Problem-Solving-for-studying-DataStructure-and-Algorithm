N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 3
# 모든 경우에 대해 3장의 카드 합을 구해야 한다.
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if max_sum < cards[i] + cards[j] + cards[k] and cards[i] + cards[j] + cards[k] <= M:
                max_sum = cards[i] + cards[j] + cards[k]
                if max_sum == M:  # 3장의 카드 합 == M:  더이상 가까워질 수 없으므로 중단
                    break

print(max_sum)