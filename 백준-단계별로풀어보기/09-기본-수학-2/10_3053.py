import sys
input = sys.stdin.readline

R = int(input())

# 허용 오차 범위가 0.0001이고, R의 최대값이 10,000이므로 적어도 0.0001 * 1/10000 * 1/10000자리까지의 원주율값이 필요하다.
print('{:.6f}'.format(R*R*3.141592653589))
print('{:.6f}'.format(R*R*2))