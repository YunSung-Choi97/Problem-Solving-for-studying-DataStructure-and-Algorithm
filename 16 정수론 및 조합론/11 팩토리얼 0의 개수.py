import sys
input = sys.stdin.readline

N = int(input())

count = 0   # N > 5^count 를 만족하는 count의 최대값. 즉 5의 거듭제곱 중 가장 큰 수의 지수
N_size = N  # count를 계산하기 위해 N값을 저장
while N_size > 4:
    N_size = N_size // 5
    count += 1

# 숫자의 뒤에 0이 있기위해서는 10의 배수가 되어야한다.
# 10의 배수가 되기위해서는 2 x 5가 있어야하므로 인수로 2와 5가 있어야한다.
# 팩토리얼을 계산하면 2의 개수가 5의 개수가 훨씬 많기때문에 5의 개수를 파악하면 10이 몇번 들어갔는지 알 수 있다.
answer = 0
for i in range(1, count+1):
    answer += N // (5 ** i)
print(answer)

'''
이 문제에서는 0 <= N <= 500이라는 조건이 있기때문에 아래 두 줄의 코드로도 해결이 가능하다.

N = int(input())
print(N//5 + N//25 + N//125)
'''