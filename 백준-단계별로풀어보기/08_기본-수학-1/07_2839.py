N = int(input())

if N in [4, 7]:  # 1, 2, 4, 7을 제외한 모든 자연수를 3과 5의 합으로 표현이 가능하다. N >= 3이므로 4와 7만 포함시켰다
    result = -1
elif N % 5 == 1:  # 마지막 (5+1)을 6으로 표현
    result = N // 5 - 1 + 2
elif N % 5 == 2:  # 마지막 (10+2)를 12로 표현
    result = N // 5 - 2 + 4
elif N % 5 == 3:  # 마지막 (5+3)를 5와 3으로 표현
    result = N // 5 + 1
elif N % 5 == 4:  # 마지막 (5+4)를 9로 표현
    result = N // 5 - 1 + 3
else:  # 3을 사용하지 않고 표현
    result = N // 5

print(result)