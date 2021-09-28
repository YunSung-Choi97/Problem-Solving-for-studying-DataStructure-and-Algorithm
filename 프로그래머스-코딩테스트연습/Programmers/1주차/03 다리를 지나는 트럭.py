from collections import deque

def solution(bridge_length, weight, truck_weights):
    N = len(truck_weights)  # 전체 트럭 수
    
    waiting_trucks = deque()  # 다리에 진입하지 않은 트럭 대기열
    for i in range(N):
        waiting_trucks.append(truck_weights[i])  # 들어갈 트럭의 (시간, 무게)
    
    time = 0
    weight_on_road = 0  # 다리 위에 있는 트럭의 무게
    truck_on_road = deque()  # 다리를 지나는 중인 트럭 (건너편에 진입하지 않은 트럭 대기열)

    IN_truck_weight = 0  # 다리에 진입할 트럭의 무게
    OUT_truck_time = 0  # 건너편으로 진입할 트럭의 도착 시간
    OUT_truck_weight = 0  # 건너편으로 진입할 트럭의 무게

    while waiting_trucks or truck_on_road or IN_truck_weight != 0 or OUT_truck_weight != 0:  # (대기중인 트럭 존재 or 다리위의 트럭 존재) and 나가기 위해 대기중인 트럭X
        # 다리로 진입할 트럭 선정
        if waiting_trucks and IN_truck_weight == 0:  # 다리 진입 대기중인 트럭 존재하는 경우
            IN_truck_weight = waiting_trucks.popleft()  # 진입 예정 트럭 무게 저장

        # 건너편으로 진입할 트럭 선정
        if truck_on_road and OUT_truck_weight == 0:  # 다리 위에 트럭 존재하는 경우
            OUT_truck_time, OUT_truck_weight = truck_on_road.popleft()  # 다리에서 빠져나갈 트럭의 (도착시간, 무게) 저장
        
        # 다리로 진입할 트럭 존재 and 하중 초과발생 X
        if IN_truck_weight != 0 and weight_on_road + IN_truck_weight <= weight:  # 도로위의 트럭무게 + 들어갈 트럭무게 <= 견디는 하중
            time += 1  # 1초 경과
            weight_on_road += IN_truck_weight  # 도로위의 트럭무게 증가
            truck_on_road.append((time + bridge_length - 1, IN_truck_weight))  # 도로위의 트럭에 추가 (빠져나갈 시간, 무게)
            IN_truck_weight = 0
        # 하중 초과발생 >> 도로 위 트럭이 지나가는 시간으로 이동
        else:
            if time < OUT_truck_time:
                time = OUT_truck_time
                weight_on_road -= OUT_truck_weight
                OUT_truck_weight = 0
        
        # 다리를 모두 건넌 트럭 이동
        if OUT_truck_weight != 0 and time >= OUT_truck_time:
            weight_on_road -= OUT_truck_weight
            OUT_truck_weight = 0
    
    # while문이 종료될 때,
    # 마지막 트럭이 다리에서 빠져나온 도착시간을 결과로 반환
    return OUT_truck_time + 1