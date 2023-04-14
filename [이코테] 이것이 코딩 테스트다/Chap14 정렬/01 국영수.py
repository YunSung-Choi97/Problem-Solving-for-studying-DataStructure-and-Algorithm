N = int(input())  # 학생의 수
score = []  # 학생들의 성적 정보: (이름, 국어, 영어, 수학)
for _ in range(N):
    name, kr, en, math = map(str, input().split())
    score.append((int(kr), int(en), int(math), name))

score.sort(key=lambda x: x[3])  # 이름 오름차순 정렬
score.sort(reverse=True, key=lambda x: x[2])  # 수학 내림차순 정렬
score.sort(key=lambda x: x[1])  # 영어 오름차순 정렬
score.sort(reverse=True, key=lambda x: x[0])  # 국어 내림차순 정렬

# 결과 출력
for i in range(N):
    print(score[i][3])

''' 입력 예시 1
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
'''
''' 출력 예시 1
Donghyuk
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
'''