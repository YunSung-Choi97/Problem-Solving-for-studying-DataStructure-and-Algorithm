def prime(n):  # 소수일때 True를 반환하는 함수
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

N = int(input())
num_list = list(map(int, input().split()))

result = 0
for i in range(N):
    if prime(num_list[i]):
        result += 1
print(result)