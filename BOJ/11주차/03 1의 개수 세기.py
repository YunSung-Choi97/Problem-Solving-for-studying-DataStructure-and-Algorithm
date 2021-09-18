# n을 2진수로 표기했을 때 길이
def Binary_size(n):
    count = 0
    while n > 0:
        n //= 2
        count += 1
    return count

# num에 대하여 2진수로 표기했을 때 k번째 자리에 1의 개수
def k_digit_count(num, k):
    # k번째 자리는 0이 2^(k-1)개, 1이 2^(k-1)개씩 반복적으로 나타난다.
    # 규칙성때문에 0부터 순서를 확인한다. 따라서, num+1 로 생각
    d = (num+1) // pow(2, k)  # 2^(k)개씩 반복.
    r = (num+1) % pow(2, k)  # d개의 묶음을 제외하고 남은 부분
    if r > pow(2, k-1):
        r = r - pow(2, k-1)
    else:
        r = 0
    
    return d * pow(2, k-1) + r

A, B = map(int, input().split())
A -= 1  # A <= N <= B {B까지 1의 개수 - (A-1)까지 1의 개수}로 해석하기 위해

A_length = Binary_size(A)
B_length = Binary_size(B)

sum_A = 0
for i in range(1, A_length+1):
    sum_A += k_digit_count(A, i)

sum_B = 0
for i in range(1, B_length+1):
    sum_B += k_digit_count(B, i)

print(sum_B - sum_A)