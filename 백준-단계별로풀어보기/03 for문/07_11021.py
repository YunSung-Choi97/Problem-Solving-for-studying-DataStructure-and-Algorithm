T = int(input())  # T : 테이트 케이스 개수

for i in range(1, T+1):  # T번 반복. i : 1 ~ T
    n, m = map(int, input().split())
    print("Case #{}: {}".format(i, n+m))  # " ".format() : 문자열에 .format을 통해 {}부분에 원하는 내용을 삽입가능