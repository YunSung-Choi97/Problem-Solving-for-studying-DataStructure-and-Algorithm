def prime(n):  # 소수일때 True를 반환하는 함수
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

M = int(input())
N = int(input())

prime_list = []  # 소수를 저장할 리스트
for i in range(M, N+1):  # 범위 내 수에 대하여 소수일 경우 prime_list에 저장
    if prime(i):
        prime_list.append(i)

if len(prime_list) == 0:  # 소수가 없는 경우
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))