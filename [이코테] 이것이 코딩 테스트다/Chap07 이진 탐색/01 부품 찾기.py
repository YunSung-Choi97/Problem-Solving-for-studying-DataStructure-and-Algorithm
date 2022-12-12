def binary_search(array, target):
    start = 0
    end = len(array) - 1

    # 이진 탐색
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:  # 찾는 값이 가운데 값보다 작은 경우
            start = mid + 1
        elif array[mid] > target:  # 찾는 값이 가운데 값보다 큰 경우
            end = mid - 1
        else:  # 찾는 값을 찾은 경우
            return mid
    return None  # 찾는 값을 못 찾은 경우

n = int(input())  # 부품 개수
data = list(map(int, input().split()))  # 전체 부품의 종류

m = int(input())  # 확인할 부품 개수
check = list(map(int, input().split()))  # 확인할 부품의 종류

data.sort()  # 부품 정렬

# 확인할 부품들 탐색 및 결과 출력
for i in range(m):
    result = binary_search(data, check[i])
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')


''' 입력 예시 1
5
8 3 7 9 2
3
5 7 9
'''
''' 출력 예시 1
no yes yes
'''