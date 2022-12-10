start = input()  # 시작 위치

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(start[0]) + 1
y = int(start[1])

dx = [1, 2, 2, 1, -1, -2, -2, -1]  # x축 이동
dy = [2, 1, -1, -2, -2, -1, 1, 2]  # y축 이동

# 8가지 방향에 대하여 이동 후 체스판 내부인지 확인
count = 0
for i in range(8):
    if 1 <= x + dx[i] <= 8 and 1 <= y + dy[i] <= 8:
        count += 1

print(count)  # 결과 출력

''' 입력 예시 1
a1
'''
''' 출력 예시 1
2
'''