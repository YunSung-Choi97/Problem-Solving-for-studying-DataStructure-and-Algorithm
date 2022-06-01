A, B, C = map(int, input().split())

# A + B * N < C * N 를 만족하는 최소의 N을 찾는 것이다.
# 따라서, A < C-B * N 이고, A // C-B < N 이다.

if B >= C:  # 만약 B가 C보다 크거나 같다면 손익분기점이 발생하지 않는다.
    print(-1)
else:
    n = A // (C - B)
    while n * (C - B) <= A:
        n += 1
    print(n)