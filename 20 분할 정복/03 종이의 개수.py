import sys
input = sys.stdin.readline

# (x0, y0) 점을 기준으로 가로/세로가 2^k0 인 사각형 내에 0만 존재하는가?
def Is_in_Only_one_value(x0, y0, k, value):
    for y in range(y0, y0 + 3**k):
        for x in range(x0, x0 + 3**k):
            if data_set[y][x] != value:
                return False
    return True

# 종이의 개수를 확인해주는 함수
def number_of_papers(x0, y0, k):
    if k != 0:
        if Is_in_Only_one_value(x0, y0, k, -1):
            answer_lst[0] += 1
        elif Is_in_Only_one_value(x0, y0, k, 0):
            answer_lst[1] += 1
        elif Is_in_Only_one_value(x0, y0, k, 1):
            answer_lst[2] += 1
        else:
            for j in range(3):
                for i in range(3):
                    number_of_papers(x0 + 3**(k-1) * i, y0 + 3**(k-1) * j, k-1)
    else:
        if data_set[y0][x0] == -1:
            answer_lst[0] += 1
        elif data_set[y0][x0] == 0:
            answer_lst[1] += 1
        elif data_set[y0][x0] == 1:
            answer_lst[2] += 1

# 입력받는 문자열의 길이
N = int(input())

# 3^k = N 을 만족하는 k
k = 0
while N != 1:
    N //= 3
    k += 1
N = 3 ** k  # N 복구

# 입력받은 데이터를 리스트에 저장
data_set = []
for _ in range(N):
    data_set.append(list(map(int, input().split())))

# 정답을 저장. (-1, 0, 1) 종이의 개수
answer_lst = [0, 0, 0]

number_of_papers(0, 0, k)  # (0, 0)부터 탐색시작
print(answer_lst[0], answer_lst[1], answer_lst[2], sep='\n')