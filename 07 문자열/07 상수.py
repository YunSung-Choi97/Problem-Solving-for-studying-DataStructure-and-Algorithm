A, B = input().split()

# R_A와 R_B에 각각 A, B를 거꾸로 저장
R_A = ''
R_B = ''
for i in range(3):
    R_A += A[2-i]
    R_B += B[2-i]

print(R_A if int(R_A) > int(R_B) else R_B)  # 큰 수를 출력