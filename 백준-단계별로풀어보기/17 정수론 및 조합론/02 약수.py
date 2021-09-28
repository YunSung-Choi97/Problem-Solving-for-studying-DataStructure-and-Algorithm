import sys
input = sys.stdin.readline

length = int(input())  # 진짜 약수의 개수
factor_lst = list(map(int, input().split()))    # 진짜 약수를 입력받아 리스트에 저장
print(max(factor_lst) * min(factor_lst))        # 진짜 약수 중 (최대값 X 최소값) 출력