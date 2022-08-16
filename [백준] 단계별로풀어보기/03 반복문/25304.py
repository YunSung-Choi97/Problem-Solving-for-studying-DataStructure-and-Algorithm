import sys
input = sys.stdin.readline

# 문제 정보 입력받기
X = int(input())  # 영수증 금액
N = int(input())  # 총 물건 종류의 수

total_payment = 0  # 실제 전체 물건 가격
for _ in range(N):
    a, b = map(int, input().split())
    total_payment += a * b

# 결과 출력
if X == total_payment:
    print('Yes')
else:
    print('No')