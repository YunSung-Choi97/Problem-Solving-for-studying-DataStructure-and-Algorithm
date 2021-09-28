T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:  # H층(꼭대기층)인 경우
        X = N // H
        Y = H
    else:
        X = N // H + 1
        Y = N % H

    print(Y, '{:0>2}'.format(X), sep='')  # Y 출력 후 두자리에 X를 출력(X가 한자리인 경우 앞에 0을 채움)