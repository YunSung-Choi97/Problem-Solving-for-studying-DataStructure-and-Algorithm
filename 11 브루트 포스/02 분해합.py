import sys
input = sys.stdin.readline

N = int(input())

exist_ans = False  # 답을 찾기 전까지는 답이 존재하지 않는다고 가정.

if N <= 18:  # else부분의 방식으로 해결할 경우 1 ~ 8과 10 ~ 17은 음수부터 확인을 하게되고, 이때 str(num)를 통해 각자릿수를 더하는 과정에서 마이너스 부호가 발생시키는 에러를 방지.
    for num in range(N):
        sum_div = num
        for i in str(num):
            sum_div += int(i)
        if sum_div == N:
            print(num)
            exist_ans = True
            break
else:  # 각 자릿수는 0 ~ 9 이므로, 생성자가 존재한다면 N-9*(N의 자릿수) ~ N 사이에 존재해야한다.
    for num in range(N-9*len(str(N)), N):
        sum_div = num
        for i in str(num):
            sum_div += int(i)
        if sum_div == N:
            print(num)
            exist_ans = True
            break
if not exist_ans:
    print(0)