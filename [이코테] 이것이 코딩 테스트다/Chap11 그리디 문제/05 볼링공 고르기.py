n, m = map(int, input().split())  # 볼링공 개수, 볼링공 최대 무게
data = list(map(int, input().split()))  # 볼링공 무게 정보

# 볼링공 무게에 따라 개수 확인
balls = [0] * (m + 1)
for i in range(n):
    balls[data[i]] += 1

# 조합 계산을 위한 팩토리얼값 저장
factorial = [1]
for i in range(1, n + 1):
    factorial.append(factorial[i - 1] * i)

# 조합 계산
def nCr(n, r):
    return factorial[n] // (factorial[n - r] * factorial[r])

# 전체 경우에서 같은 공을 꺼내는 경우 제외
result = nCr(n, 2)
for i in range(1, m + 1):
    if balls[i] != 1:
        result -= nCr(balls[i], 2)

print(result)  # 결과 출력

''' 입력 예시 1
5 3
1 3 2 3 2
'''
''' 출력 예시 1
8
'''

''' 입력 예시 2
8 5
1 5 4 3 2 4 5 2
'''
''' 출력 예시 2
25
'''