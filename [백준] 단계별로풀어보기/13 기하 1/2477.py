import sys
input = sys.stdin.readline

# 문제정보 입력받기
K = int(input())
border = []  # 둘레 방향 정보 저장
length = []  # 둘레 길이 정보 저장
for _ in range(6):
    b, l = map(int, input().split())
    border.append(b)
    length.append(l)

# 밭은 형태에 따라 가장 긴 가로길이와 가장 긴 세로길이의 인덱스 확인
if border.count(1) == 1 and border.count(3) == 1:
    large_width_idx = border.index(1)
    large_height_idx = border.index(3)
elif border.count(1) == 1 and border.count(4) == 1:
    large_width_idx = border.index(1)
    large_height_idx = border.index(4)
elif border.count(2) == 1 and border.count(3) == 1:
    large_width_idx = border.index(2)
    large_height_idx = border.index(3)
elif border.count(2) == 1 and border.count(4) == 1:
    large_width_idx = border.index(2)
    large_height_idx = border.index(4)

# 큰 사각형의 가로, 세로 길이 및 밭이 아닌 작은 사각형의 가로, 세로 길이 저장
large_width = length[large_width_idx]
large_height = length[large_height_idx]
small_width = abs(length[(large_height_idx + 1) % 6] - length[(large_height_idx - 1) % 6])
small_height = abs(length[(large_width_idx + 1) % 6] - length[(large_width_idx - 1) % 6])
# 결과 출력
print(K * (large_width * large_height - small_width * small_height))