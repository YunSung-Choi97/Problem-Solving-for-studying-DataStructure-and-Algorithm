def solution(N, stages):
    people = len(stages)  # 전체 플레이어 수

    # 스테이지에 따라 계수 정렬
    stage_people = [0 for _ in range(N + 2)]  # 인덱스 통일을 위해 0은 무시, N + 1 개의 stage 생성
    for stage in stages:
        stage_people[stage] += 1
    
    failure_rate = []  # 실패율
    for i in range(1, N + 1):
        # 해당 단계를 진행중인 사람이 없는 경우 실패율 0
        if stage_people[i] == 0:
            failure_rate.append((0, i))
        # 해당 단계를 진행중인 사람 수 / 이후 단계를 진행중인 사람 수
        else:    
            failure_rate.append((stage_people[i] / people, i))
            people -= stage_people[i]

    failure_rate.sort(reverse=True, key=lambda x: x[0])  # 실패율을 기준으로 정렬 (실패율이 같은 경우 단계별로 저장했기 때문에 오름차순)

    # 실패율에 따른 단계만 정답에 저장
    answer = []
    for i in range(N):
        answer.append(failure_rate[i][1])

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
''' 입력 예시 1
5, [2, 1, 2, 6, 2, 4, 3, 3]
'''
''' 출력 예시 1
[3, 4, 2, 1, 5]
'''

print(solution(4, [4, 4, 4, 4, 4]))
''' 입력 예시 1
4, [4, 4, 4, 4, 4]
'''
''' 출력 예시 1
[4, 1, 2, 3]
'''