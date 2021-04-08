import sys
input = sys.stdin.readline

def Only_0(_x0, _y0, k0):
    for y in range(_y0, _y0 + 2**k0):
        for x in range(_x0, _x0 + 2**k0):
            if data_set[y][x] == 1:
                return False
    return True

def Only_1(_x0, _y0, k0):
    for y in range(_y0, _y0 + 2**k0):
        for x in range(_x0, _x0 + 2**k0):
            if data_set[y][x] == 0:
                return False
    return True

N = int(input())    # 입력받는 정사각형 한변의 길이

k = 0               # 2^k = N 을 만족하는 k
while N != 1:
    N //= 2
    k += 1
N = 2 ** k

data_set = []       # 입력받은 데이터를 이차원 리스트형태로 저장
for _ in range(N):
    data = list(map(int, input().split()))
    data_set.append(data)

test_lst = [[0, 0, k]]  # 같은 수로 채워져 있는지 확인해야하는 리스트 (시작 x좌표, 시작 y좌표, 변의 길이(k))
answer_lst = []         # 같은 수로 채워져 있는 리스트 (시작 x좌표, 시작 y좌표, 변의 길이(2^k), 채워진 수)

while len(test_lst) != 0:       # test_lst가 비어있을 때까지 반복
    x0, y0, k = test_lst[0]
    if Only_0(x0, y0, k):       # 0으로 채워져있는가?
        answer_lst.append([x0, y0, 2**k, 0])
    elif Only_1(x0, y0, k):     # 1으로 채워져있는가?
        answer_lst.append([x0, y0, 2**k, 1])
    else:                       # 0과 1이 섞여있는 경우
        if k != 1:  # 한 변의 길이가 2보다 클때(k>1).
            test_lst.append([x0, y0, k-1])
            test_lst.append([x0, y0 + 2**(k-1), k-1])
            test_lst.append([x0 + 2**(k-1), y0, k-1])
            test_lst.append([x0 + 2**(k-1), y0 + 2**(k-1), k-1])
        else:
            if data_set[y0][x0] == 0:
                answer_lst.append([x0, y0, 1, 0])
            else:
                answer_lst.append([x0, y0, 1, 1])
            
            if data_set[y0+1][x0] == 0:
                answer_lst.append([x0, y0+1, 1, 0])
            else:
                answer_lst.append([x0, y0+1, 1, 1])
            
            if data_set[y0][x0+1] == 0:
                answer_lst.append([x0+1, y0, 1, 0])
            else:
                answer_lst.append([x0+1, y0, 1, 1])
            
            if data_set[y0+1][x0+1] == 0:
                answer_lst.append([x0+1, y0+1, 1, 0])
            else:
                answer_lst.append([x0+1, y0+1, 1, 1])
    del(test_lst[0])  # 확인한 정사각형 삭제

count0 = 0  # 0으로 채워진 정사각형 개수
count1 = 0  # 1으로 채워진 정사각형 개수
for answer in answer_lst:
    if answer[3] == 0:
        count0 += 1
    else:
        count1 += 1

print(count0)
print(count1)