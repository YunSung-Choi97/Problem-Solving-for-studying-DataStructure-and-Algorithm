N, M, K = map(int, input().split())
N_number = list(map(int, input().split()))
N_number.sort()
result = 0

while M > 0:
    count = K
    while M > 0 and count - 1 > 0:
        result += N_number[-1]
        M -= 1
        count -= 1
    
    if M > 0:
        result += N_number[-2]
        M -= 1

print(result)