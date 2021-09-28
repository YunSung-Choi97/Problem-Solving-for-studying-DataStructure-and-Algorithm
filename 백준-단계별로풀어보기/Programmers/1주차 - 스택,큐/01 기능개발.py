def solution(progresses, speeds):
    days = []
    size_function = len(progresses)

    for i in range(size_function):
        R = 100 - progresses[i]
        if R % speeds[i] == 0:
            days.append(R // speeds[i])
        else:
            days.append(R // speeds[i] + 1)
    
    answer = []

    time = -1
    for i in range(size_function):
        if time < days[i]:
            time = days[i]
            answer.append(1)
        else:
                answer[-1] += 1

    return answer