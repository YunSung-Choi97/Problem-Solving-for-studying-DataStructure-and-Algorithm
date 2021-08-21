import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 3
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if max_sum < cards[i] + cards[j] + cards[k] and cards[i] + cards[j] + cards[k] <= M:
                max_sum = cards[i] + cards[j] + cards[k]
                if max_sum == M:
                    break

print(max_sum)