import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

R_AC = A % C
R = 1
R_lst = []
find_cycle = False
for _ in range(B):
    R = (R * R_AC) % C
    if not R in R_lst:
        R_lst.append(R)
    else:
        find_cycle = True
        cycle_start_index = R_lst.index(R)
        break

if find_cycle:
    if (B - cycle_start_index) % (len(R_lst) - cycle_start_index) == 0:
        answer_index = len(R_lst) - 1
    else:
        answer_index = cycle_start_index + (B - cycle_start_index) % (len(R_lst) - cycle_start_index) - 1
else:
    answer_index = R_lst[B-1]

print(R_lst[answer_index])