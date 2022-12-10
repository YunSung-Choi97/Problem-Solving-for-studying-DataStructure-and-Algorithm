n, m = map(int, input().split())  # 행의 개수, 열의 개수

# n행 m열의 배열 입력받기
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 각 행에서 가장 작은 수 저장
min_numbers = []
for y in range(n):
    min_numbers.append(min(array[y]))

print(max(min_numbers))  # 결과 출력

''' 입력 예시 1
3 3
3 1 2
4 1 4
2 2 2
'''
''' 출력 예시 1
2
'''

''' 입력 예시 2
2 4
7 3 1 8
3 3 3 4
'''
''' 출력 예시 2
3
'''