T = int(input())

for i in range(T):
    R, S = input().split()
    for j in S:  # 문자열 S에서 한글자씩 불러와
        for k in range(int(R)):  # R번 만큼 반복
            print(j, end='')  # 출력
    print()