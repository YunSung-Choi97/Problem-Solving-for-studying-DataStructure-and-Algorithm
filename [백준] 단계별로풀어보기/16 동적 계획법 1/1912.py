import sys
input = sys.stdin.readline

# 문제정보 입력받기
n = int(input())
array = list(map(int, input().split()))

# 최대값을 저장하는 수열
result = [array[0]]
max_result = array[0]
for i in range(1, n):
    result.append(max(result[i - 1] + array[i], array[i]))
    if max_result < result[i]:
        max_result = result[i]

# 결과 출력
print(max_result)