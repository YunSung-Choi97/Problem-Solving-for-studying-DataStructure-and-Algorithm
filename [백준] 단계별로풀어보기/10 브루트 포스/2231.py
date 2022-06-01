N = int(input())

exist_ans = False  # 답을 찾기 전까지는 답이 존재하지 않는다고 가정.

# 각 자릿수는 0 ~ 9 이므로, 생성자가 존재한다면 N - 9*(N의 자릿수) ~ N 사이에 존재
if N > 18:
    for num in range(N-9*len(str(N)), N):
        sum_div = num
        for i in str(num):
            sum_div += int(i)
        if sum_div == N:
            print(num)
            exist_ans = True
            break
# N이 1 ~ 18인 경우 : 1부터 N까지 분해합 확인
else:  # 1 ~ 18은 위의 방법으로 해결 시 -9, -18을 하면서 (-)가 에러를 유발
    for num in range(1, N):
        sum_div = num
        for i in str(num):
            sum_div += int(i)
        if sum_div == N:
            print(num)
            exist_ans = True
            break

if not exist_ans:  # 생성자가 없는 경우
    print(0)