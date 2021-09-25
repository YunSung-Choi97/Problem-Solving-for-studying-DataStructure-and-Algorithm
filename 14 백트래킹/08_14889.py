'''미리 생각하기
1. 입력받기 (N, N x N 크기의 2차원 리스트)
2. 팀 나누기 >> N명 중 0.5N명 뽑기
3. 점수 계산
4. 팀원 변경 << BackTracking
'''
import sys
input = sys.stdin.readline

# 입력받기
N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]

# 하나의 팀의 팀원이 모두 결정되면 나머지 팀의 팀원도 결정되므로 한 팀만 구성
team = [False] * N

# 팀의 전체 능력치 계산
def team_ability_gap():
    team1, team2 = list(), list()  # 팀1과 팀2로 구분
    for i in range(N):
        if team[i]:
            team1.append(i)
        else:
            team2.append(i)
    
    ability1, ability2 = 0, 0  # 팀1의 능력치와 팀2의 능력치 구하기
    for i in range(N // 2):
        for j in range(N // 2):
            if i == j:
                continue
            ability1 += ability[team1[i]][team1[j]]
            ability2 += ability[team2[i]][team2[j]]
    
    return abs(ability1 - ability2)

# 팀 구성하기
def make_team(k):
    if team.count(True) == N // 2:  # 0.5N명의 팀원이 정해진 순간
        global min_gap, flag
        min_gap = min(min_gap, team_ability_gap())
        if min_gap == 0:
            flag = True
        return
    
    for i in range(k, N):
        team[i] = True  # i를 팀에 추가
        make_team(i+1)
        if flag: return
        team[i] = False  # i를 팀에서 제거

min_gap = 50 * N  # 능력치 차이의 최소값 (능력치는 최대 100, 팀원은 최대 0.5N명이므로 50N으로 초기화)
flag = False  # min_gap이 0이 되면 더 작아질 수 없기때문에 탐색 중단 flag
make_team(0)
print(min_gap)