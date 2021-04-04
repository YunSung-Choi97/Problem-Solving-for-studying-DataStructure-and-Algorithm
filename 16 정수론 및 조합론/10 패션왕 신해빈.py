import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    
    clothes = []  # 의상 종류를 저장
    for i in range(n):
        clothes.append(input().split()[-1])
    
    kind = []   # 의상 종류를 저장 (중복X)
    count = []  # 같은 의상 종류의 개수를 저장
    for i in range(n):
        if not clothes[i] in kind:
            kind.append(clothes[i])
            count.append(clothes.count(clothes[i]))
    
    # 전체 = (의상 종류1 개수 + 1) x (의상 종류2 개수 + 1) x ... x (의상 종류k 개수 + 1) - 1  단, 여기서 k는 kind의 크기
    answer = 1
    for i in count:
        answer *= i+1

    print(answer-1)