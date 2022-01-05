A, B, C = map(int, input().split())

# 일반적인 연산 순서가 반영되어있다.
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)