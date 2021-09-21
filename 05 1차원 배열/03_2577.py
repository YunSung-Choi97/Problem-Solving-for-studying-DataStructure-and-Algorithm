# 자연수 A, B, C를 사용자로부터 입력받음
A = int(input())
B = int(input())
C = int(input())

num = str(A * B * C)  # A * B * C 의 결과를 문자열로 바꿔 num에 할당
for i in range(10):  # 각각의 인덱스에 각 숫자가 몇번 사용되었는지 확인
    print(num.count('{}'.format(i)))