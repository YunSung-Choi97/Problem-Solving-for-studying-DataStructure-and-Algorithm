n, m = map(int, input().split())  # 처음 팀의 수, 연산 횟수
team = [i for i in range(n + 1)]  # i번 학생의 팀 번호

# 팀 합치기
def union_team(a, b):
    # 이미 같은 팀인 경우 종료
    if team[a] == team[b]:
        return
    # b를 a팀으로 합치기
    team[b] = team[a]

# 나의 팀장 찾기
def find_team(a):
    if team[a] != a:
        team[a] = find_team(team[a])
    return team[a]

# 같은 팀인지 확인하기
def same_team(a, b):
    teamA = find_team(a)
    teamB = find_team(b)
    if teamA == teamB:
        return True
    else:
        return False

# 연산 수행 및 결과 출력    
for _ in range(m):
    oper, a, b = map(int, input().split())  # 연산, 학생 a, 학생 b
    # 팀 합치기 수행
    if oper == 0:
        union_team(a, b)
    # 같은 팀 여부 확인
    else:
        if same_team(a, b):
            print('YES')
        else:
            print('NO')

''' 입력 예시 1
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''
''' 출력 예시 1
NO
NO
YES
'''