N, X = map(int, input().split())  # N, X : 입력받을 정수의 개수, 기준이 되는 수
lst = list(map(int, input().split()))  # 입력받은 수들을 lst에 할당

for i in range(N):  # N번 반복
    if lst[i] < X:
        print(lst[i], end = " ")  # 출력 후 줄바꿈이 아닌 공백을 출력