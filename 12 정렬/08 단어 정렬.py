import sys
input = sys.stdin.readline

words = []
N = int(input())
for _ in range(N):
    word = input().strip()  # 입력에서 줄바꿈 제거
    words.append(word)
words = list(set(words))  # 동일한 단어를 제거하기위해 set으로 한번 변환해준 뒤 다시 list로 변환

words.sort()
words.sort(key=lambda word : len(word))  # words내의 길이를 기준으로 정렬
for answer in words:
    print(answer)