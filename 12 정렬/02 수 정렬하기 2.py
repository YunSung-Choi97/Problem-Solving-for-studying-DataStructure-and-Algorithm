import sys
input = sys.stdin.readline

N = int(input())
num_data = []  # N개의 숫자를 입력받아 저장
for _ in range(N):
    num_data.append(int(input()))

num_data.sort()  # N개의 수를 오름차순으로 정렬
for num in num_data:
    print(num)