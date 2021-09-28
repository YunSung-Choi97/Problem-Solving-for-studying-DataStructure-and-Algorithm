# 런타임 에러 (NameError) 발생

# 문제의 2번째 해결 방식과 큰 차이가 없다고 생각했지만, 런타임 에러가 발생.
# 두 방식의 차이는 최댓값의 초기화와 첫번째 인덱스 처리이다.
# 아래 코드를 실행하면 반드시 max_num은 초기화가 된 후 크기비교를 하기 때문에, 왜 런타임 에러가 발생한지 잘 모르겠다.
# 이는 백준에서는 런타임 에러로 처리되었지만, 다른 프로그램에서는 정상적으로 동작했다.

for i in range(1, 10):
    num = int(input())
    if i == 1:
        max_num = num
    if max_num < num:
        max_num = num
        index = i
print(max_num, index, sep = '\n')