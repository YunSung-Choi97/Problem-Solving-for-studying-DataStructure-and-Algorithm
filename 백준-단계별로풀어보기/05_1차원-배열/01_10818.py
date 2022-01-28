N = int(input())  # N : 입력 받을 정수 개수

lst = list(map(int, input().split()))  # lst : 입력받은 정수들을 저장한 리스트. 입력받은 데이터를 정수형으로 만들어준 후 맵핑해준것을 리스트화 해준다
lst.sort()  # 오름차순 정리
print(lst[0], lst[-1])  # 0번째 인덱스와 -1번째 인덱스(마지막) 출력

# print(min(s:=[*map(int,[*open(0)][1].split())]),max(s))