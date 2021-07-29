def solution(food_times, k):

    if sum(food_times) <= k:
        answer = -1

    else:
        N = len(food_times)
        i = 0
        while k > 0:
            if food_times[i] != 0:
                food_times[i] -= 1
                k -= 1
            if i == N - 1:
                i = 0
            else:
                i += 1
        
        while food_times[i] == 0:
            if i == N - 1:
                i = 0
            else:
                i += 1

        answer = i + 1

    return answer

print(solution([3, 1, 2], 5))