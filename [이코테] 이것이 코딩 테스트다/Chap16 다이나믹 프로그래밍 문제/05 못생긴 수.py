N = int(input())  # 찾는 못생긴 수 번호

if N <= 5:
    print(N)
else:
    ugly_num = [False, True, True, True, True, True]  # index가 못생긴 수인가?
    count = 5  # 발견한 못생긴 수의 개수
    last = 5  # 못생긴 수인지 확인한 마지막 수

    # N개의 못생긴 수를 찾을때까지 반복
    while N > count:
        # 새로운 못생긴 수를 찾을때까지 반복
        while True:
            last += 1
            if last % 2 == 0 and ugly_num[last // 2]:
                ugly_num.append(True)
                count += 1
                break
            elif last % 3 == 0 and ugly_num[last // 3]:
                ugly_num.append(True)
                count += 1
                break
            elif last % 5 == 0 and ugly_num[last // 5]:
                ugly_num.append(True)
                count += 1
                break
            # 못생긴 수가 아닌 경우
            else:
                ugly_num.append(False)

    print(len(ugly_num) - 1)  # 결과 출력