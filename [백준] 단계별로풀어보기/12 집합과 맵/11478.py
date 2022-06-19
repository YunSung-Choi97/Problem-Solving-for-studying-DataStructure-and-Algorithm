import sys
input = sys.stdin.readline

# 문제정보 입력받기
S = input().rstrip()
result = set()

# 문자열 길이에 따라 부분 문자열을 집합에 추가하기
for length in range(1, len(S) + 1):
    for i in range(len(S) - length + 1):
        result.add(S[i:i+length])

# 결과 출력
print(len(result))