import sys
input = sys.stdin.readline

N = int(input())

def factorial(n):
    if n == 1:
        return 1
    else:
        answer = 1
        for i in range(1, n+1):
            answer *= i
        return answer

# factorial = [1 for _ in range(N+1)]
# for i in range(1, N+1):
#     factorial[i] = i * factorial[i-1]

# N!를 구한 후 문자열로 바꿔 -1 index부터 0의 개수를 확인
number = str(factorial(N))
count = 0
for i in range(-1, -1 * (len(number)+1), -1):
    if number[i] == '0':
        count += 1
    else:
        break
print(count)