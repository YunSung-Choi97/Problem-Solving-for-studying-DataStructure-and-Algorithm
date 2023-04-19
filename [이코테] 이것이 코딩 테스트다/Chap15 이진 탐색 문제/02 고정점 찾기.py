def find_fixed_point():
    left, right = 0, len(An) - 1  # 왼쪽 인덱스, 오른쪽 인덱스
    while left <= right:
        center = (left + right) // 2  # 중간 인덱스
        # 고정점을 찾은 경우 탐색 종료
        if center == An[center]:
            return center
        # 인덱스가 값보다 큰 경우
        elif center > An[center]:
            left = center + 1
        # 인덱스가 값보다 작은 경우
        else:
            right = center - 1
    
    # 고정점을 찾지 못한 경우 -1 반환
    return -1

N = int(input())  # 수의 개수
An = list(map(int, input().split()))  # 수열 (오름차순 정렬 상태)

print(find_fixed_point())  # 결과 출력

''' 입력 예시 1
5
-15 -6 1 3 7
'''
''' 출력 예시 1
3
'''

''' 입력 예시 2
7
-15 -4 2 8 9 13 15
'''
''' 출력 예시 2
2
'''

''' 입력 예시 2
7
-15 -4 3 8 9 13 15
'''
''' 출력 예시 2
-1
'''