import sys
input = sys.stdin.readline

S = input()
size = len(S)

start_zero = 0
while S[start_zero] == '0':
    start_zero += 1

result = 0

if size-1 == start_zero:
    print(result)
else:
    result += int(S[start_zero])

for i in range(start_zero + 1, size):
    if S[i] != '0':
        result = result * int(S[i])
    else:
        continue

print(result)