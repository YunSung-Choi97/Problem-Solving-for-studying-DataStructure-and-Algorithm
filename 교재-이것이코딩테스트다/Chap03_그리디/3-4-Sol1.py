# 단순하게 푸는 답안 예시
# N의 범위가 커진다면, N이 K의 배수가 되도록 효율적으로 한번에 빼는 방식으로 작성하는 것이 좋다.

# N, K을 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)