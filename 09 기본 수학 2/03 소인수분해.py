N = int(input())

result = []  # 소수를 저장할 리스트
while N != 1:
    for i in range(2, N+1):
        if N % i == 0:
            result.append(i)
            N //= i
            break

for prime_factor in result:
    print(prime_factor)