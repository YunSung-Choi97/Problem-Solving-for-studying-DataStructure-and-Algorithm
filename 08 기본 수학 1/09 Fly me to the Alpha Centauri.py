import math  # 올림(math.ceil)을 사용하기 위해 불러움

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    dis = y - x  # 이동할 거리
    max_dis = math.ceil(pow(dis, 0.5))  # 이동할 거리의 제곱근 올림값
    if dis > (pow(max_dis, 2) + pow(max_dis-1, 2)) // 2:
        print(2 * max_dis - 1)
    else:
        print(2 * max_dis - 2)
        
    # 1 2 3 4 5 5 4 3 2 1
    # 3 : 1 1 1
    # 4 : 1 2 1
    # 5 : 1 2 1 1
    # 6 : 1 2 2 1
    # 7 : 1 2 2 1 1
    # 8 : 1 2 2 2 1
    # 9 : 1 2 3 2 1
    #10 : 1 2 3 2 1 1
    #11 : 1 2 3 2 2 1
    #12 : 1 2 3 3 2 1
    #13 : 1 2 3 3 2 1 1
    #14 : 1 2 3 3 2 2 1
    #15 : 1 2 3 3 3 2 1
    #16 : 1 2 3 4 3 2 1
    #17 : 1 2 3 4 3 2 1 1