def solution(food_times, k):
    if sum(food_times) <= k:
        answer = -1
        return answer

    else:
        N = len(food_times)
        sorted_food_time = sorted(food_times)
        
        count = 0
        last_time = 0
        sum_of_time = 0
        for idx, time in enumerate(sorted_food_time):
            if count < time:
                count = time
                if k >= sum_of_time + (count-last_time)*len(sorted_food_time[idx:]):
                    sum_of_time += (count-last_time)*len(sorted_food_time[idx:])
                    last_time = count
                else:
                    break
        
        rest = k - sum_of_time
        i = 0
        rest_time = []
        for idx, time in enumerate(food_times):
            if time >= count:
                rest_time.append((idx+1))
        
        return rest_time[rest % len(rest_time)]

        # while True:
        #     rest -= 1
        #     if rest == -1:
        #         return rest_time[i]
        #     if i != len(rest_time)-1:
        #         i += 1
        #     else:
        #         i = 0

for i in range(20):
    print(solution([3, 2, 4, 2], i), i)