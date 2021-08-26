import sys
input = sys.stdin.readline

people = []
N = int(input())
for _ in range(N):
    age, name = input().split()
    people.append((age, name))

people.sort(key=lambda human : int(human[0]))  # 나이를 기준으로 정렬
for human in people:
    print(human[0], human[1])