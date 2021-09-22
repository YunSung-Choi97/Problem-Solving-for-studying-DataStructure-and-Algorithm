num = input().strip()

result = sorted(num, reverse=True)  # 내림차순으로 정렬한 리스트를 반환.
for i in result:
    print(i, end='')