import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = list(map(int, input().split()))

balls = [0 for i in range(11)]

for i in range(1, 11):
    balls[i] = K.count(i)

result = 0
for i in range(1, 10):
    temp = 0
    for j in range(i+1, 11):
        temp += balls[j]
    result += (temp * balls[i])

print(result)