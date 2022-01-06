def is_prime(n):  # n이 소수일때 True를 반환하는 함수
    if n == 1:
        return False
    elif n == 2:
        return True
    # n의 제곱근까지 약수가 없다면 그 이후에도 약수가 존재하지 않는 점을 이용
    check_point = int(n**0.5) + 1
    count = 0
    for i in range(2, check_point+1):
        if n % i == 0:
            count += 1
            break
    if count == 0:
        return True
    else:
        return False

M, N = map(int, input().split())
for i in range(M, N+1):
    if is_prime(i):
        print(i)