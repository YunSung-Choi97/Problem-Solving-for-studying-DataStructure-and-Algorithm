def nCr(n, r):  # 조합이 필요하여 nCr을 계산해줄 함수 제작
    temp_mul = 1  # 최종 분자
    temp_dev = 1  # 최종 분모
    if n < 2 * r:  # nCr = nC(n-r)이고, 계산과정을 줄이기 위해 추가
        r = n - r

    for i in range(r):
        temp_mul *= (n-i)
        temp_dev *= (i+1)
    
    return temp_mul // temp_dev

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    # (0층) 1, 2, 3, 4, 5, 6, ... 1 1 1 1 1
    # (1층) 1, 3, 6, 10, 15, 21, ... 2 3 4 5 6
    # (2층) 1, 4, 10, 20, 35, 56, ... 3 6 10 15 21
    # (k층) ... , k+n C n-1 >> 2층 6호 : 8C5 = 8 7 6 / 3 2 1
    print(nCr(k+n, n-1))