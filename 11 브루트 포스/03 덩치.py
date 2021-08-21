import sys
input = sys.stdin.readline

N = int(input())
body_data = []  # (몸무게, 키) 정보를 저장
for _ in range(N):
    kg, cm = map(int, input().split())
    body_data.append((kg, cm))

for kg, cm in body_data:  # 한 명씩 본인보다 더 무겁고 키가 큰 사람의 수를 확인
    big = 0
    for other_kg, other_cm in body_data:
        if kg < other_kg and cm < other_cm:
            big += 1
    print(big+1, end=' ')