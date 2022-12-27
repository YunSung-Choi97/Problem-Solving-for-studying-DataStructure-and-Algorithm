from itertools import permutations

def solution(n: int, weak: list, dist: list):
    count = [0] * n  # i번 위치까지 존재하는 취약 지점 개수
    count[0] = 1 if 0 in weak else 0
    for i in range(1, n):
        count[i] = count[i - 1] + 1 if i in weak else count[i - 1]

    dist.sort(reverse=True)  # 긴 거리를 확인할 수 있는 친구를 우선적으로 채용하기 위해 내림차순 정렬
    for friend_num in range(1, len(dist) + 1):  # 일할 친구 수를 한명씩 늘려가며 확인
        work = dist[:friend_num]
        work = list(map(list, permutations(work, friend_num)))  # 점검 시작할 모든 경우의 수
        size = len(work) // 2 if len(work) > 1 else 1  # (절반은 순서가 다르지만 원이라 동일한 경우라 제거)
        for distance in work[:size]:  # 일할 친구을 확정시켜 확인
            for start in weak:  # 각 취약 지점에서 점검을 시작하며 확인
                find_answer = True  # 답을 못 찾은 경우에 False로 수정
                curr_distance = distance.copy()

                check_length = 0  # 현재 점검한 길이
                location = start  # 현재 점검 중인 위치
                while check_length < n:  # 모든 구역을 점검할 때까지 점검
                    if location in weak:  # 현재 위치가 취약 지점인 경우
                        if curr_distance:  # 점검할 다음 친구가 있는 경우
                            check =  curr_distance.pop()
                            check_length += (check + 1)  # 이동 거리 추가
                            location = (location + check + 1) % n  # 이동
                        else:
                            find_answer = False  # 취약 지점을 점검할 친구가 없기 때문에 실패
                            break
                    else:
                        if count[location] + 1 in count:  # 다음 취약지점이 12시 지점을 지나기 전에 있는 경우
                            next_location = count.index(count[location] + 1)
                            check_length += (next_location - location)  # 이동 거리 추가
                            location = next_location  # 이동
                        else:
                            check_length += n - location  # 이동 거리 추가
                            location = 0  # (12시 지점으로) 이동

                if find_answer:
                    return friend_num

    return -1

''' 입력 예시 1
12, [1, 5, 6, 10], [1, 2, 3, 4]
'''
''' 출력 예시 1
2
'''

''' 입력 예시 2
12, [1, 3, 4, 9, 10], [3, 5, 7]
'''
''' 출력 예시 2
1
'''