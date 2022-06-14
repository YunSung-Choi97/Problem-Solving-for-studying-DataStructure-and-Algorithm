import sys
input = sys.stdin.readline

# 문제정보 입력받기
N = int(input())
my_cards = set(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))

result = []  # 결과를 저장할 리스트
for card in cards:
    if card in my_cards:
        result.append(1)
    else:
        result.append(0)
print(*result)

'''
# my_cards 정보를 list 형식으로 저장했을 때 위와 같은 방법은 시간초과가 발생하기 때문에 이분탐색 이용해 해결가능하다.

# 이분탐색 함수
def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if target < array[mid]:
            end = mid - 1
        elif target > array[mid]:
            start = mid + 1
        else:
            return 1

    return 0

# 문제정보 입력받기
N = int(input())
my_cards = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))

my_cards.sort()  # 이분탐색을 위해 오름차순 정렬
result = []  # 결과를 저장할 리스트
for card in cards:
    result.append(binary_search(my_cards, card))
print(*result)
'''