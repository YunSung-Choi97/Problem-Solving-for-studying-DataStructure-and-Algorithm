import sys
input = sys.stdin.readline

fibonacci = [[0, 0] for i in range(41)]  # fibonacci[n] = [0이 호출되는 횟수, 1이 호출되는 횟수]
fibonacci[0] = [1, 0]  # 초기값 할당
fibonacci[1] = [0, 1]  # 초기값 할당
for i in range(2, 41):
    fibonacci[i][0] = fibonacci[i - 2][0] + fibonacci[i - 1][0]
    fibonacci[i][1] = fibonacci[i - 2][1] + fibonacci[i - 1][1]

T = int(input())  # test case의 수
for _ in range(T):
    N = int(input())
    print(fibonacci[N][0], fibonacci[N][1])