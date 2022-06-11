N = int(input())

# 길이에 따라 만들어진 계단수의 1의 자리 개수
result = [[0 for i in range(10)] for j in range(N + 1)]

# 한 자리 수 초기화
for i in range(1, 10):
    result[1][i] = 1

# 이미 만들어진 수에 일의 자리 수를 추가하는 형태로 계단수 제작
for idx in range(2, N + 1):
    result[idx][0] = result[idx - 1][1]
    result[idx][9] = result[idx - 1][8]
    for i in range(1, 9):
        result[idx][i] = (result[idx - 1][i - 1] + result[idx - 1][i + 1]) % 1000000000

# 정답 출력
print(sum(result[N]) % 1000000000)