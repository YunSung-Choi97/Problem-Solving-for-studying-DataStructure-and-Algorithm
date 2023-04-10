# dfs방식으로 연산자 끼워넣기 수행
def dfs(previous, operator, next):
    # 마지막 연산인 경우
    if next == N - 1:
        if operator[0] != 0:  # 덧셈
            result[0] = max(result[0], previous + An[next])
            result[1] = min(result[1], previous + An[next])
        if operator[1] != 0:  # 뺄셈
            result[0] = max(result[0], previous - An[next])
            result[1] = min(result[1], previous - An[next])
        if operator[2] != 0:  # 곱셈
            result[0] = max(result[0], previous * An[next])
            result[1] = min(result[1], previous * An[next])
        if operator[3] != 0:  # 나눗셈
            if previous < 0 and An[next] > 0:  # 음수를 양수로 나누는 경우
                result[0] = max(result[0], -(-previous // An[next]))
                result[1] = min(result[1], -(-previous // An[next]))
            else:
                result[0] = max(result[0], previous // An[next])
                result[1] = min(result[1], previous // An[next])
    # 마지막 연산이 아닌 경우
    else:
        if operator[0] != 0:  # 덧셈
            dfs(previous + An[next], [operator[0] - 1, operator[1], operator[2], operator[3]], next + 1)
        if operator[1] != 0:  # 뺄셈
            dfs(previous - An[next], [operator[0], operator[1] - 1, operator[2], operator[3]], next + 1)
        if operator[2] != 0:  # 곱셈
            dfs(previous * An[next], [operator[0], operator[1], operator[2] - 1, operator[3]], next + 1)
        if operator[3] != 0:  # 나눗셈
            if previous < 0 and An[next] > 0:  # 음수를 양수로 나누는 경우
                dfs(-(-previous // An[next]), [operator[0], operator[1], operator[2], operator[3] - 1], next + 1)
            else:
                dfs(previous // An[next], [operator[0], operator[1], operator[2], operator[3] - 1], next + 1)

N = int(input())  # 수의 개수
An = list(map(int, input().split()))  # A1, A2, ..., An
operator = list(map(int, input().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈 연산자의 개수

result = [-1e9, 1e9]  # 결과 저장
dfs(An[0], operator, 1)  # 연산자 끼워넣기 시작

print(result[0], result[1], sep='\n')  # 결과 출력

''' 입력 예시 1
2
5 6
0 0 1 0
'''
''' 출력 예시 1
30
30
'''

''' 입력 예시 2
3
3 4 5
1 0 1 0
'''
''' 출력 예시 2
35
17
'''

''' 입력 예시 3
6
1 2 3 4 5 6
2 1 1 1
'''
''' 출력 예시 3
54
-24
'''