import sys
import math

# 반지름 입력받기
R = int(sys.stdin.readline())

# 반지름이 R인 원의 넓이 출력
print('{:.6f}'.format(math.pi*R*R))  # 유클리드 기하학
print('{:.6f}'.format(2*R*R))  # 택시 기하학