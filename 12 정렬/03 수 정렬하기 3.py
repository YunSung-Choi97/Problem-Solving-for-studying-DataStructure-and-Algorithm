import sys
input = sys.stdin.readline

# 입력받는 수는 굉장히 많지만, 수의 범위가 작기때문에 카운팅 정렬을 이용

N = int(input())
num_data = {i : 0 for i in range(1, 10001)}  # key가 1 ~ 10000이고 각각의 value가 0인 dict 생성

# 입력받은 수에 해당하는 key의 value를 1씩 더함
for _ in range(N):
    num = int(input())
    num_data[num] += 1

# key값을 value번씩 반복하여 출력
for key, value in num_data.items():
    for _ in range(value):
        print(key)

'''
# dict를 사용하지않고, dict의 key를 list의 index로 생각하고 동일한 방법으로 해결.
# [BOJ 제출결과] dict 풀이 : 29964KB, 9840ms / list 풀이 : 29708KB, 9572ms / 시간은 제출에 따라 조금씩 변함.
N = int(input())
num_data = [0 for i in range(10001)]

for _ in range(N):
    num = int(input())
    num_data[num] += 1

for idx, value in enumerate(num_data):
    for _ in range(value):
        print(idx)
'''