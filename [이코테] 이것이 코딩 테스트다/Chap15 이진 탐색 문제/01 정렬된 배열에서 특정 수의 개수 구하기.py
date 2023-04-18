# 이진탐색을 통한 찾는 값의 첫번째 인덱스 찾기
def find_first_index(x):
    # 이진 탐색
    left, right = 0, len(An) - 1  # 왼쪽 인덱스, 오른쪽 인덱스
    first_index = -1  # 찾는 값의 첫번째 인덱스
    while left <= right:
        center = (left + right) // 2  # 중간 인덱스
        # 찾는 값이 중간 값보다 작은 경우 왼쪽 영역 탐색
        if x < An[center]:
            right = center - 1
        # 찾는 값이 중간 값보다 큰 경우 오른쪽 영역 탐색
        elif An[center] < x:
            left = center + 1
        # 찾는 값을 찾은 경우 왼쪽 영역 탐색
        else:
            first_index = center
            right = center - 1
    
    return first_index

# 이진탐색을 통한 찾는 값의 마지막 인덱스 찾기
def find_last_index(x):
    # 이진 탐색
    left, right = 0, len(An) - 1  # 왼쪽 인덱스, 오른쪽 인덱스
    last_index = -1  # 찾는 값의 마지막 인덱스
    while left <= right:
        center = (left + right) // 2  # 중간 인덱스
        # 찾는 값이 중간 값보다 작은 경우 왼쪽 영역 탐색
        if x < An[center]:
            right = center - 1
        # 찾는 값이 중간 값보다 큰 경우 오른쪽 영역 탐색
        elif An[center] < x:
            left = center + 1
        # 찾는 값을 찾은 경우 오른쪽 영역 탐색
        else:
            last_index = center
            left = center + 1

    return last_index

N, x = map(int, input().split())  # 수의 개수, 찾는 수
An = list(map(int, input().split()))  # 수열 (오름차순 정렬 상태)

first, last = find_first_index(x), find_last_index(x)  # 찾는 수의 첫번째/마지막 인덱스

# 찾는 값이 없는 경우 -1 출력
if first == -1:
    print(-1)
else:
    print(last - first + 1)

''' 입력 예시 1
7 2
1 1 2 2 2 2 3
'''
''' 출력 예시 1
4
'''

''' 입력 예시 2
7 4
1 1 2 2 2 2 3
'''
''' 출력 예시 2
-1
'''