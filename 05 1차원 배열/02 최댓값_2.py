# 1차원 배열을 이용하지 않고 최댓값만 저장해 계산
max_num = 0  # max_num : 입력받은 자연수 중 최댓값을 저장할 변수
for i in range(1, 10):  # 9번 반복. 1 ~ 9번째 자연수 확인
    num = int(input())
    if max_num < num:
        max_num = num
        index = i
print(max_num, index, sep = '\n')



# 위의 방식과 큰 차이가 없다고 생각했지만, 런타임 에러가 발생.
# 입력받는 수가 자연수라는 조건을 고려하지 않았을 때, 최댓값의 초기화가 어렵다고 생각해 첫번째 입력값으로 초기화를 해야겠다고 생각을 했다.
# 이때, 반복 횟수가 크게 늘어난다면 필요없는 검사가 많아지기 때문에 굉장히 비효율적이겠지만, 총 9번으로 정해져있었기 때문에 런타임 에러가 발생하지 않을 것이라 예상한 것과는 다른 결과였다.

# for i in range(1, 10):
#     num = int(input())
#     if i == 1:
#         max_num = num
#     if max_num < num:
#         max_num = num
#         index = i
# print(max_num, index, sep = '\n')