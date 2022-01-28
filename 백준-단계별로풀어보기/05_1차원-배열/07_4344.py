C = int(input())  # 테스트 케이스 개수

for _ in range(C):
    data = list(map(int, input().split()))  # 입력 데이터

    N = data[0]                 # 학생 수
    score_lst = data[1:]        # 학생 점수 

    aver = sum(score_lst) / N   # 학생 평균

    over_aver = 0               # 학생 평균을 넘는 사람 수
    for score in score_lst:
        if score > aver:
            over_aver += 1
    
    rate_over_aver = over_aver / N * 100  # 학생 평균을 넘는 사람 비율(퍼센트)

    print("{:.3f}%".format(rate_over_aver))