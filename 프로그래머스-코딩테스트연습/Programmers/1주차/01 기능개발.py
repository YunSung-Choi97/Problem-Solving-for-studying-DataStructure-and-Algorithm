def solution(progresses, speeds):
    days = []  # 최소로 필요한 수행 기간
    size_function = len(progresses)  # 작업의 개수

    for i in range(size_function):
        R = 100 - progresses[i]  # 남은 작업량
        if R % speeds[i] == 0:  # 최소로 필요한 수행 시간 저장
            days.append(R // speeds[i])
        else:
            days.append(R // speeds[i] + 1)
    
    answer = []

    # 더 큰 값이 나타나면 answer에 1을 넣어주고, 아닐 경우 마지막값에 1을 더함.
    time = -1
    for i in range(size_function):
        if time < days[i]:
            time = days[i]
            answer.append(1)
        else:
            answer[-1] += 1

    return answer