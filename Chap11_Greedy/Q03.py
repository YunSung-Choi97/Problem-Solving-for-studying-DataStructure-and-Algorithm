S = input()

zero = 0
one = 0

target = S[0]
for char in S:
    if char == target:
        if target == '0':
            zero += 1
            target = '1'
        else:
            one += 1
            target = '0'

print(min(zero, one))