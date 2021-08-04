N = input()

N_2 = len(N) // 2

left_N = int(N[:N_2])
right_N = int(N[N_2:])

left_sum = 0
right_sum = 0
for i in range(N_2):
    left_sum += (left_N // pow(10, i) % 10)
    right_sum += (right_N // pow(10, i) % 10)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")