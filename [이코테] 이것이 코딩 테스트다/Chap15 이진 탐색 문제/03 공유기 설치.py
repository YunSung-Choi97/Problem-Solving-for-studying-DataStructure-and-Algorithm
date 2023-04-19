import sys

N, C = map(int, input().split())  # 집의 개수, 설치할 공유기 개수
house = []  # 집의 위치
for _ in range(N):
    house.append(int(sys.stdin.readline()))

house.sort()  # 집의 위치 오름차순 정렬

min_interval = 1  # 공유기 사이의 최소 간격
max_interval = (house[-1] - house[0]) // (C - 1)  # 공유기 사이의 최대 간격: 가장 멀리 떨어진 두 집 사이 거리를 (공유기 개수 - 1)등분

answer = 1  # 최소 간격 1로 가정
# 최소 간격과 최대 간격 사이의 값 중 C개 이상 공유기 설치가 가능한 최대 간격 이분 탐색
while min_interval <= max_interval:
    interval = (min_interval + max_interval) // 2  # 공유기 사이의 간격

    # 설정된 간격으로 공유기 설치
    last_router, count = house[0], 1  # 첫 번째 집에 공유기 설치
    for i in range(1, N):
        # 현재 방문한 집이 이전 공유기로부터 interval 이상 떨어진 경우 공유기 추가 설치
        if house[i] >= last_router + interval:
            last_router, count = house[i], count + 1
    
    # 공유기가 C개보다 적게 설치된 경우
    if count < C:
        max_interval = interval - 1  # 최대 간격을 현재 간격보다 줄이고 다시 확인
    # 공유기가 C개 이상 설치된 경우
    else:
        answer = interval  # 현재 간격 저장
        min_interval = interval + 1  # 최소 간격을 현재 간격보다 늘려서 다시 확인

print(answer)  # 결과 출력

''' 입력 예시 1
5 3
1
2
8
4
9
'''
''' 출력 예시 1
3
'''