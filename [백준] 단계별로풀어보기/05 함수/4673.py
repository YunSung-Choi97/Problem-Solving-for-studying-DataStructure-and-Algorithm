def d_number(n):
    size = 1        # n의 자릿수
    n_for_size = n  # n의 자릿수를 구하기 위한 임시 수
    # n의 자릿수 알아내기
    while True:
        if n_for_size // 10 == 0:
            break
        n_for_size //= 10
        size += 1
    
    # result에 n과 n의 각 자릿수 더하기
    result = n
    for i in range(size):
        result += (n // pow(10, i)) % 10

    return result

# 1 ~ 10000을 갖는 리스트에서 모든 d(n)을 제거
self_num = [i for i in range(1, 10001)]
for i in range(1, 10000):
    if d_number(i) in self_num:
        self_num.remove(d_number(i))

# 결과 출력
for num in self_num:
    print(num)