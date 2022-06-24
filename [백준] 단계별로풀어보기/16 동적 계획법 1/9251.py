# 문제정보 입력받기
An = input()
Bn = input()

# LCS를 저장할 2차원 배열 생성
n = len(An)
m = len(Bn)
LCS = [[0 for x in range(n + 1)] for y in range(m + 1)]

# LCS 계산
for y in range(1, m + 1):
    for x in range(1, n + 1):
        # 글자가 같은 경우 1 증가
        if An[x - 1] == Bn[y - 1]:  # 주의 : 배열과 문자열의 인덱스가 동일하지 않음
            LCS[y][x] = LCS[y - 1][x - 1] + 1
        # 글자가 다른 경우 위와 동일하게 처리할 경우 LCS의 길이를 손해볼 수 있음
        else:
            LCS[y][x] = max(LCS[y][x - 1], LCS[y - 1][x])

# 결과 출력
print(LCS[-1][-1])