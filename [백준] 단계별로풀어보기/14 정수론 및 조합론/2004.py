import sys
input = sys.stdin.readline

# n! 인수에 num의 개수를 파악하는 함수
def num_count(n, num):
    answer = 0
    while n != 0:
        n //= num
        answer += n
    return answer

n, m = map(int, input().split())

if m == 0:
    print(0)
else: 
    # 2의 개수와 5의 개수 중 작은 값을 정답으로 출력
    print(min(num_count(n, 2)-num_count(m, 2)-num_count(n-m, 2), num_count(n, 5)-num_count(m, 5)-num_count(n-m, 5)))

# 팩토리얼을 계산해서, 또는 조합을 계산해서 문제를 풀게되면 시간초과 혹은 메모리 초과 등의 결과가 나오게 된다.