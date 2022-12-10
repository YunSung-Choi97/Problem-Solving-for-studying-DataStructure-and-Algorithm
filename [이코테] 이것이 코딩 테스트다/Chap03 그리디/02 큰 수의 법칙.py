n, m, k = map(int, input().split())  # 배열의 크기, 숫자가 더해지는 횟수, 같은 수 연속 덧셈 가능 횟수
array = list(map(int, input().split()))  # 입력받은 배열

array.sort(reverse=True)  # 가장 큰 수와 두 번째로 큰 수를 찾기위해 정렬

result = 0  # 큰 수의 법칙 결과
count = 0  # 같은 수 연속 덧셈 횟수
for i in range(m):
    if count == k:
        result += array[1]
        count = 0
        continue
    result += array[0]
    count += 1
    
print(result)  # 결과 출력

''' 입력 예시 1
5 8 3
2 4 5 4 6
'''
''' 출력 예시 1
46
'''