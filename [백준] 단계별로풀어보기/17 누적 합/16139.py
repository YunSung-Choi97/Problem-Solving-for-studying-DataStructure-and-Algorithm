import sys
input = sys.stdin.readline

# 문제정보 입력받기
S = input().rstrip()
q = int(input())

# 각 글자 자리에 대하여 알파벳 개수 누적 합 계산
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = [0] * 26
prefix_sum = [None] * len(S)
for i in range(len(S)):
    count[alphabet.index(S[i])] += 1
    prefix_sum[i] = count.copy()

# 결과 출력
for _ in range(q):
    a, l, r = input().split()
    idx = alphabet.index(a)
    if int(l) == 0:
        print(prefix_sum[int(r)][idx])
    else:
        print(prefix_sum[int(r)][idx] - prefix_sum[int(l) - 1][idx])