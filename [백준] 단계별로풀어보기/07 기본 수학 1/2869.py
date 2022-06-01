A, B, V = map(int, input().split())

if A == V:  # 첫날 모두 올라가는 경우
    print(1)
else:
    result = (V-A) // (A-B)
    # 정확히 다 올라가는 경우와 그렇지 않은 경우 분리
    if result*(A-B) + A < V:
        print(result+2)
    else:
        print(result+1)