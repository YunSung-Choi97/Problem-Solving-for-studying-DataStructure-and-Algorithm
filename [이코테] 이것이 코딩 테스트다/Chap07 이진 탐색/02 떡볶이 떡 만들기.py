def binary_search(array, target):
    start = 0
    end = max(array)

    length = 0  # 딱 맞는 길이를 찾지 못했을 때 자를 최댓값
    # 이진 탐색
    while start <= end:
        mid = (start + end) // 2

        result = 0  # 잘리는 떡 길이 합
        for i in range(len(array)):
            if array[i] > mid:
                result += array[i] - mid

        if result < target:  # 찾는 값이 가운데 값보다 작은 경우
            end = mid - 1
            length = mid
        elif result > target:  # 찾는 값이 가운데 값보다 큰 경우
            start = mid + 1
        else:  # 찾는 값을 찾은 경우
            return mid
    return length  # 찾는 값을 못 찾은 경우

n, m = map(int, input().split())  # 떡의 개수, 요청한 떡의 길이
length = list(map(int, input().split()))  # 떡의 길이 정보

print(binary_search(length, m))  # 결과 출력

''' 입력 예시 1
4 6
19 15 10 17
'''
''' 출력 예시 1
15
'''