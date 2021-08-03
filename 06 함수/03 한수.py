N = int(input())

# 100미만의 수는 모두 한수이다.
if N < 100:
    print(N)
# 100이상의 수에 대하여 한수 찾기
else:
    result = 99
    for n in range(100, N+1):
        sub_100_10 = n // 100 - (n // 10) % 10  # 100의 자릿수 - 10의 자릿수
        sub_10_1 = (n // 10) % 10 - n % 10      # 10의 자릿수 - 1의 자릿수
        if sub_100_10 == sub_10_1:  # 두 수가 같다면 한수
            result += 1
    print(result)