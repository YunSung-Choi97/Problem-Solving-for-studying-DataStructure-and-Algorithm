from collections import deque

def solution(bridge_length, weight, truck_weights):
    N = len(truck_weights)
    
    waiting_trucks = deque()
    for i in range(N):
        waiting_trucks.append(truck_weights[i])  # 들어갈 트럭의 (시간, 무게)
    
    time = 0
    weight_on_road = 0
    truck_on_road = deque()
    IN_weight = 0
    OUT_time = 0

    while waiting_trucks or truck_on_road:
        if IN_weight == 0:
            IN_weight = waiting_trucks.popleft()

        if weight_on_road + IN_weight <= weight:
            time += 1
            weight_on_road += IN_weight
            truck_on_road.append((time + bridge_length, IN_weight))
            IN_weight = 0
        else:
            pass
        
        if OUT_time == 0:
            t, w = truck_on_road.popleft()

            

    for i in range(N):
        if weight_on_road + truck_weights[i] <= weight:
            time += 1
            weight_on_road += truck_weights[i]
            truck_on_road.append((time, truck_weights[i]))


    



    answer = 0
    return answer