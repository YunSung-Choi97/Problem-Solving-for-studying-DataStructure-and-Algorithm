import sys
input = sys.stdin.readline

# 입력받기 및 저장
Country = tuple(input().split())
Data = []
for _ in range(6):
    A, B, W, D, L = input().split()
    Data.append((A, B, W, D, L))

# 나라 간 경기 발생하는 모든 경기 결과와 승점 나타내기
# gameN : 경기한 국가에 승/무/패에 맞는 승점과 확률 저장
game1 = [[0 for i in range(5)] for j in range(3)]  # ex1) game1 = [[3, 0, 0, 0, 1.0], [1, 1, 0, 0, 0.0], [0, 3, 0, 0, 0.0]]
game2 = [[0 for i in range(5)] for j in range(3)]  # ex2) game2 = [[0, 0, 0, 3, 0.428], [0, 0, 1, 1, 0.144], [0, 0, 3, 0, 0.428]]
game3 = [[0 for i in range(5)] for j in range(3)]
game4 = [[0 for i in range(5)] for j in range(3)]
game5 = [[0 for i in range(5)] for j in range(3)]
game6 = [[0 for i in range(5)] for j in range(3)]
games = [game1, game2, game3, game4, game5, game6]  # games = [[[0 for i in range(5)] for j in range(3)] for k in range(6)]

win_point = [(3, 0), (1, 1), (0, 3)]  # 승점 (승/무/패)

for i in range(len(Data)):
    player1 = Data[i][0]
    player2 = Data[i][1]
    for j in range(3):
        games[i][j][Country.index(player1)], games[i][j][Country.index(player2)] = win_point[j]
        games[i][j][4] = float(Data[i][j+2])

# 모든 경우에 대하여 조별 예선을 통과하는 나라의 확률 확인
total = [0, 0, 0, 0]  # 모든 경우에 대한 최종 결과확률

for g1 in game1:
    for g2 in game2:
        for g3 in game3:
            for g4 in game4:
                for g5 in game5:
                    for g6 in game6:
                        # 6경기 결과 (점수, 확률)
                        score = [0, 0, 0, 0]  # 6경기의 승점 결과
                        for i in range(4):
                            score[i] += g1[i] + g2[i] + g3[i] + g4[i] + g5[i] + g6[i]
                        probability = g1[4] * g2[4] * g3[4] * g4[4] * g5[4] * g6[4]  # 6경기의 결과가 일어날 확률
                        if probability == 0:
                            continue
                        
                        # 순위 확인
                        rank = [1, 1, 1, 1]  # 경기 결과에 따른 조별리그 등수
                        for i in range(4):
                            count = 0
                            for j in range(4):
                                if score[i] < score[j]:
                                    count += 1
                            rank[i] += count
                        
                        # 순위에 따른 승점 가능성
                        if rank.count(1) == 1:  # 1등 1명
                            total[rank.index(1)] += probability
                            if rank.count(2) == 1:  # 2등 1명
                                total[rank.index(2)] += probability
                            else:
                                for i in range(4):
                                    if rank[i] == 2:
                                        total[i] += probability / rank.count(2)
                        elif rank.count(1) == 2:  # 1등 2명
                            for i in range(4):
                                if rank[i] == 1:
                                    total[i] += probability
                        else:
                            for i in range(4):
                                if rank[i] == 1:
                                    total[i] += 2 * probability / rank.count(1)

for P in total:
    print('{:.10f}'.format(P))