import sys
input = sys.stdin.readline

def make_star(n):
    if n == 3:  # 초기 조건 (크기가 3X3인 경우)
        stars = [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]
        return stars

    else:  # 크기가 3X3이 아닌 경우
        stars = [[' ' for j in range(n)] for i in range(n)]
        

        k = n // 3
        mini_stars = make_star(k)  # 한 사이즈 작은 별(1/3 크기의 별)이 8개가 나타난다.
        for y in range(k):
            for x in range(k):
                stars[y][x] = mini_stars[y][x]
                stars[y][x+k] = mini_stars[y][x]
                stars[y][x+2*k] = mini_stars[y][x]
                stars[y+k][x] = mini_stars[y][x]
                stars[y+k][x+2*k] = mini_stars[y][x]
                stars[y+2*k][x] = mini_stars[y][x]
                stars[y+2*k][x+k] = mini_stars[y][x]
                stars[y+2*k][x+2*k] = mini_stars[y][x]
        return stars

N = int(input())

star = make_star(N)
for i in range(N):
    print(''.join(star[i]))  # 구분자.join(리스트) : 리스트의 요소를 구분자(문자형)로 연결하여 문자열로 반환