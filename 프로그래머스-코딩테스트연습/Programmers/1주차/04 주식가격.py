def solution(prices):
    size = len(prices)  # 주식 가격의 수

    answer = [size-(i+1) for i in range(size)]  # 끝날때까지의 기간 저장 (감소하는 구간이 없는 경우)
    for i in range(size-1):
        for j in range(i+1, size):
            if prices[i] > prices[j]:  # 감소하는 구간이 있는 경우
                answer[i] = j - i  # 기간의 길이로 변경
                break
    
    return answer