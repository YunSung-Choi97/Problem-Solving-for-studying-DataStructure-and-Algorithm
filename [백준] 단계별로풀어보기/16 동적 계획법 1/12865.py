import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # N(물품 수), K(가능한 최대 무게) 입력받기

bag = [0] * (K + 1)
for _ in range(N):
    W, V = map(int, input().split())  # W(무게), V(가치) 입력받기
    for i in range(K, W - 1, -1):
        bag[i] = max(bag[i], bag[i - W] + V)  # 새로 들어온 물건으로 최대 가치 수정

# 결과 출력
print(bag[-1])