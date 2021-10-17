import sys
input = sys.stdin.readline

N = int(input())
Pn = list(map(int, input().split()))
Pn.sort()  # 오름차순으로 정렬. 먼저 인출하는 사람의 시간이 짧을수록 전체 대기시간 값이 짧아지기 때문에

result = 0
for i in range(N):
    result += Pn[i] * (N-i)

print(result)