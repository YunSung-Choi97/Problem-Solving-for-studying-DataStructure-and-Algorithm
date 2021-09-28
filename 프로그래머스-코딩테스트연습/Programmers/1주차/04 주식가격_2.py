def solution(prices):
    size = len(prices)  # 주식 가격의 수

    decrease = [False] * size  # 감소하는 구간이 존재하는가?
    answer = []
    for i in range(size - 1):
        for j in range(i+1, size):
            if prices[i] > prices[j]:
                answer.append(j-i)
                decrease[i] = True  # 감소하는 지점이 존재
                break
        if not decrease[i]:  # 감소하는 지점이 존재하지 않는다면 (길이 - index - 1) 추가
            answer.append(size-1-i)
    answer.append(0)  # 마지막 주식 결과
    
    return answer