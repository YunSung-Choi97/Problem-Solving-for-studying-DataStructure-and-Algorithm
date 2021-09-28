# 1/1
# 1/2 2/1
# 3/1 2/2 1/3
# 1/4 2/3 3/2 4/1
# 5/1 ... 4/2

N = int(input())

k = 1
count = 0
while True:
    count += k
    if N <= count:
        shift = N - (count - k)  # 해당 층에서 몇 칸을 이동해야하는지
        if k % 2 == 1:  # 홀수층과 짝수층의 규칙이 다름
            print((k+1)-shift, '/', shift, sep='')
        else:
            print(shift, '/', (k+1)-shift, sep='')
        break
    else:
        k += 1