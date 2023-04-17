N = int(input())  # 집의 수
house = list(map(int, input().split()))  # 집의 위치

farthest = max(house)  # 가장 먼 집의 위치

# 위치별 집의 개수 저장
location = [0 for _ in range(farthest + 1)]
for i in range(N):
    location[house[i]] += 1

# 위치별 집의 위치 누적합
sum_of_location = [0 for _ in range(farthest + 1)]
for i in range(1, farthest + 1):
    sum_of_location[i] = sum_of_location[i - 1] + location[i] * i

answer, sum_of_distance = 0, 2e5 * 1e5  # 안테나 설치 위치, 안테나로부터 모든 집까지의 거리의 총 합
count = 0  # 현재 위치까지 집의 개수
for i in range(1, farthest + 1):
    # i 위치에 집이 없는 경우 안테나 설치 불가
    if location[i] == 0:
        continue
    count += location[i]  # 현재 위치까지의 집의 개수 갱신
    # 안테나로부터 모든 집까지의 거리의 총 합
    # = 각각의 집에 대하여 |집의 위치 - 안테나의 위치|
    # = 각각의 집에 대하여 (안테나 위치 - 안테나 위치값보다 작은 집의 위치) + (안테나 위치값보다 큰 집의 위치 - 안테나 위치)
    distance = (i * count - sum_of_location[i]) + ((sum_of_location[farthest] - sum_of_location[i]) - i * (N - count))
    # 거리의 총 합이 더 작은 경우 안테나 설치
    if distance < sum_of_distance:
        answer = i
        sum_of_distance = distance

# 결과 출력
print(answer)

''' 입력 예시 1
4
5 1 7 9
'''
''' 출력 예시 1
5
'''