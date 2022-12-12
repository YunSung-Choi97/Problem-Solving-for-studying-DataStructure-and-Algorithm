n = int(input())  # 학생 수

students = []  # 학생들의 성적 데이터 저장
for _ in range(n):
    student = input().split()
    students.append((student[0], int(student[1])))

students.sort(key=lambda student: student[1])  # 성적을 기준으로 정렬

# 결과 출력
for student in students:
    print(student[0], end=' ')

''' 입력 예시 1
2
홍길동 95  
이순신 77
'''
''' 출력 예시 1
이순신 홍길동
'''