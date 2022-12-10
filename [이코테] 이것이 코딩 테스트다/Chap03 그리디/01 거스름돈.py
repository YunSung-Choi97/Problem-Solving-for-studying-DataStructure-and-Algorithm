n = int(input())  # 거슬러 줘야 할 돈
coins = [500, 100, 50, 10]  # 가진 동전 종류

count = 0  # 거슬러 줘야 할 동전의 개수
for coin in coins:
    count += n // coin
    n %= coin

print(count)  # 결과 출력

''' 입력 예시 1
1260
'''
''' 출력 예시 1
6
'''