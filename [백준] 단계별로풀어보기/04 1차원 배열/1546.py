N = int(input())  # 과목의 개수
grade_lst = list(map(int, input().split()))  # 과목들의 성적을 저장하는 리스트

aver = 0  # 성적의 평균
for i in range(N):
    aver += grade_lst[i]
aver = aver / N

new_aver = aver / max(grade_lst) * 100  # 새로운 평균
print(new_aver)