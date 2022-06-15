import sys
input = sys.stdin.readline

# 문제정보 입력받기
N, M = map(int, input().split())

name_idx, num_idx = dict(), dict()  # 포켓몬 이름을 key로 하는 딕셔너리, 포켓몬 번호를 key로 하는 딕셔너리
for i in range(1, N + 1):
    name = input().rstrip()
    name_idx[name] = i
    num_idx[i] = name

for _ in range(M):
    Question = input().rstrip()
    # 문제가 숫자인지 확인 후 정답 출력
    try:
        print(num_idx[int(Question)])
    except:
        print(name_idx[Question])