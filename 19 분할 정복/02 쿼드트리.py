import sys
input = sys.stdin.readline

def Only_0(_x0, _y0, k0):
    for y in range(_y0, _y0 + 2**k0):
        for x in range(_x0, _x0 + 2**k0):
            if data_set[y][x] == '1':
                return False
    return True

def Only_1(_x0, _y0, k0):
    for y in range(_y0, _y0 + 2**k0):
        for x in range(_x0, _x0 + 2**k0):
            if data_set[y][x] == '0':
                return False
    return True

def QuadTree(x0, y0, k0):
    if k0 != 0:
        if Only_0(x0, y0, k0):       # 0으로 채워져있는가?
            print('0', end='')
        elif Only_1(x0, y0, k0):     # 1으로 채워져있는가?
            print('1', end='')
        else:
            print('(', end='')
            QuadTree(x0, y0, k0 - 1)
            QuadTree(x0 + 2**(k0-1), y0, k0 - 1)
            QuadTree(x0, y0 + 2**(k0-1), k0 - 1)
            QuadTree(x0 + 2**(k0-1), y0 + 2**(k0-1), k0 - 1)
            print(')', end='')
    else:
        print('{}'.format(data_set[y0][x0]), end='')

N = int(input())    # 입력받는 문자열의 길이

k = 0               # 2^k = N 을 만족하는 k
while N != 1:
    N //= 2
    k += 1
N = 2 ** k

data_set = []       # 입력받은 데이터를 리스트에 저장
for _ in range(N):
    data = input()
    data_set.append(data[:-1])

QuadTree(0, 0, k)