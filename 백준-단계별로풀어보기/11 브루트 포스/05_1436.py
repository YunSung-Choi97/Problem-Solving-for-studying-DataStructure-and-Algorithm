N = int(input())

positional_number = [str(i) for i in range(10)]  # 0 ~ 9 : 각각의 자릿수에 사용
target_numbers = {'666'}  # 666이 포함된 숫자를 저장할 집합 (자릿수의 길이에 따라 업데이트됨)

while True:
    # 만든 타켓수가 더 많은 경우 정렬
    if len(target_numbers) >= N:
        target_numbers = sorted(target_numbers)
        break

    # 이미 만들어진 타겟수에 앞 또는 뒤에 0~9를 붙여 한자리 긴 타켓수들을 제작
    temp = set([])  # 중복제거를 위해 집합으로 제작.  ex) 666에 앞 또는 뒤에 '6'을 더하여 만들어진 '6666'과 '6666'을 하나로 생각
    for p_n in positional_number:
        for num in target_numbers:
            temp.add(num + p_n)
            temp.add(p_n + num)
    target_numbers = temp

print(target_numbers[N-1])