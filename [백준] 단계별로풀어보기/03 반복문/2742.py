N = int(input())  # N : 출력하고자하는 자연수의 마지막값

for i in range(N):  # N번 반복 (i는 0부터 N-1까지)
    print(N - i)

# for i in range(N, 0, -1):  # N번 반복 (i는 N부터 1까지 -1씩 변화)
#     print(i)