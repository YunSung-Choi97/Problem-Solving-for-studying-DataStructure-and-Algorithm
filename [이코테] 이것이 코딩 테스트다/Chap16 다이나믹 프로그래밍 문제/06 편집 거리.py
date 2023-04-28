strA = input()  # 문자열 A
strB = input()  # 문자열 B

lenA, lenB = len(strA), len(strB)  # 문자열의 길이

# dp 테이블 초기화
dp = [[0 for x in range(lenA + 1)] for y in range(lenB + 1)]
for x in range(lenA + 1):
    dp[0][x] = x
for y in range(lenB + 1):
    dp[y][0] = y

# 한글자씩 확인하며 편집
for y in range(1, lenB + 1):
    for x in range(1, lenA + 1):
        # 문자가 같은 경우
        if strA[x - 1] == strB[y - 1]:
            dp[y][x] = dp[y - 1][x - 1]
        # 문자가 다른 경우
        else:
            dp[y][x] = min(dp[y][x - 1], dp[y - 1][x], dp[y - 1][x - 1]) + 1
    
print(dp[-1][-1])  # 결과 출력