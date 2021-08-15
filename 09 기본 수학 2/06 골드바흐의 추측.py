import sys
import math
input = sys.stdin.readline

def make_prime_list(n):
    prime_list = [True for i in range(n+1)]
    prime_list[0] = False
    prime_list[1] = False
    for i in range(2, math.ceil(n**0.5)+1):
        if prime_list[i]:
            for j in range(2*i, n+1, i):
                prime_list[j] = False
    return prime_list

T = int(input())
num_list = [int(input()) for _ in range(T)]  # 입력받은 수들을 저장하는 리스트
prime_list = make_prime_list(max(num_list))  # 입력받은 수 중 최대값까지 소수 판별

for num in num_list:
    prime_numbers = []  # 해당 수까지의 소수 리스트
    for i in range(num+1):
        if prime_list[i]:
            prime_numbers.append(i)
    
    find_center = num  # 중간값과 가까운 값 찾기
    for i in range(len(prime_numbers)):
        if find_center > abs(num // 2 - prime_numbers[i]):
            find_center = abs(prime_numbers[i] - num // 2)
            center = i
        else:
            break
    
    for i in range(center, -1, -1):
        if num - prime_numbers[i] in prime_numbers:
            ans1 = prime_numbers[i]
            ans2 = num - prime_numbers[i]
            break
    
    print(min(ans1, ans2), max(ans1, ans2))