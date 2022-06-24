import sys
input = sys.stdin.readline

# 문제정보 입력받기
n = int(input())
line = list()
for _ in range(n):
    A, B = map(int, input().split())
    line.append((A, B))
line.sort()

# 전봇대 위에서부터 최대한 전깃줄을 많이 연결
left = [1] * n
for i in range(n):
    for j in range(i - 1, -1, -1):
        if line[j][1] < line[i][1] and left[j] + 1 > left[i]:
            left[i] = left[j] + 1

# 전봇대 아래에서부터 최대한 전깃줄을 많이 연결
right = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if line[i][1] < line[j][1] and right[i] < right[j] + 1:
            right[i] = right[j] + 1

# 제거한 전깃줄의 수 = 전체 전깃줄의 수 - 꼬이지 않고 최대한 연결한 전깃줄의 수
print(n - max(max(left), max(right)))