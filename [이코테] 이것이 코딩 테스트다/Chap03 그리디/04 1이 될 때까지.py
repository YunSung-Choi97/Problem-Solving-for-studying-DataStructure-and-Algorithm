n, k = map(int, input().split())  # 문제의 n과 k 입력받기

count = 0  # 필요한 연산의 최소 횟수
while n != 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1
    count += 1

print(count)  # 결과 출력

''' 입력 예시 1
25 5
'''
''' 출력 예시 1
2
'''