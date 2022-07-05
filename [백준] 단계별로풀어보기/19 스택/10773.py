import sys
input = sys.stdin.readline

K = int(input())  # K 입력받기
storage = list()  # 입력받은 수를 저장할 리스트

for _ in range(K):
    num = int(input())
    if num == 0:
        storage.pop()
    else:
        storage.append(num)

# 결과 출력
print(sum(storage))