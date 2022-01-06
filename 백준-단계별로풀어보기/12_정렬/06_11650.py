import sys
input = sys.stdin.readline

N = int(input())
xy_data = []
for _ in range(N):
    x, y = map(int, input().split())
    xy_data.append((x, y))

# xy_data에서 각각의 1번 인덱스 값으로 오름차순 정렬을 한 뒤 0번 인덱스 값으로 오름차순 재정렬
xy_data.sort(key=lambda num : num[1])
xy_data.sort()
for i in range(N):
    print(xy_data[i][0], xy_data[i][1])