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

input_num_list = []
while True:
    n = int(input())
    if n == 0:
        break
    input_num_list.append(n)

# 입력된 수들 중 가장 작은 수보다 큰 수 ~ 가장 큰 수의 2배 사이의 값에 대하여 미리 소수인지 확인
prime_list = [False for i in range(2*max(input_num_list)+1)]
for i in range(min(input_num_list)+1, 2*max(input_num_list)+1):
    if is_prime(i):
        prime_list[i] = True

for num in input_num_list:
    count = 0
    for i in range(num+1, 2*num+1):
        if prime_list[i]:
            count += 1
    print(count)

''' 처음 시도한 방식 : 입력된 수마다 문제풀이 >> 시간 초과
while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n+1, 2*n+1):  # n 초과 ~ 2n 이하의 수에 대하여 확인
        if is_prime(i):
            count += 1
    print(count)
'''