N = int(input())  # N : 구구단의 단을 입력 받음

for i in range(1, 10):  # i에 1, 2, 3, ... , 8, 9까지 할당하며 아래의 동작 수행
    print("{} * {} = {}".format(N, i, N*i))  # {}에 format()내의 값들을 차례로 하나씩 넣어줌