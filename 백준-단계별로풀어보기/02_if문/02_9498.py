grade = int(input())  # grade : 시험 점수를 입력받음

# 문제의 조건에 맞게 조건을 나눠서 학점을 출력
if 90 <= grade <= 100:
    print("A")
elif 80 <= grade:  # 초기에 80 <= grade < 90: 로 작성을 했으나, 점수는 0~100점이고 위의 조건을 제외한 grade의 범위는 0~89이므로 이와 같이 작성해도 동일하다. 위의 90~100 구간도 동일하게 수정 가능하다.
    print("B")
elif 70 <= grade:
    print("C")
elif 60 <= grade:
    print("D")
else:
    print("F")