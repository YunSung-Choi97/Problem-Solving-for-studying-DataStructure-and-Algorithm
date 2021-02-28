N = int(input())  # N : 출력할 별의 줄 수

for i in range(1, N+1):  # N번 반복. i : 1 ~ N
    print("{}".format("*"*i))  # " ".format() : 문자열에 .format을 통해 {}부분에 원하는 내용을 삽입가능