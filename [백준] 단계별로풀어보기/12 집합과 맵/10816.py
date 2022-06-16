import sys
input = sys.stdin.readline

# 문제정보 입력받기
N = int(input())
temp = list(map(int, input().split()))
my_cards = dict()  # dict 형식으로 내 카드 정보 저장
for card in temp:
    if my_cards.get(card) == None:
        my_cards[card] = 1
    else:
        my_cards[card] += 1
M = int(input())
check_cards = list(map(int, input().split()))

# 결과 확인하며 정답 출력
for card in check_cards:
    if my_cards.get(card) == None:
        print(0, end=' ')
    else:
        print(my_cards[card], end=' ')