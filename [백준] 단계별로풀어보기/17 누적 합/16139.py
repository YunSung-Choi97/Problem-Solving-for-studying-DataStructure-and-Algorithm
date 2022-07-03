import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input())

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = [0] * 26
prefix_sum = [None] * len(S)
for i in range(len(S)):
    count[alphabet.index(S[i])] += 1
    prefix_sum[i] = count.copy()

for _ in range(q):
    a, l, r = map(str, input().split())
    idx = alphabet.index(a)
    print(prefix_sum[int(r)][idx] - prefix_sum[int(l)][idx])