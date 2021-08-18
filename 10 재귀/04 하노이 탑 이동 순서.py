import sys
input = sys.stdin.readline

def hanoi_top(n):
    if n == 1:
        process = [[1, 3]]
        return process
    
    else:
        pre_process = hanoi_top(n-1)
        front_process = [[int, int] for i in range(2**(n-1)-1)]
        back_process = [[int, int] for i in range(2**(n-1)-1)]

        for i in range(2**(n-1)-1):
            for j in range(2):
                if pre_process[i][j] == 1:
                    front_process[i][j] = 1
                    back_process[i][j] = 2
                elif pre_process[i][j] == 2:
                    front_process[i][j] = 3
                    back_process[i][j] = 1
                else:
                    front_process[i][j] = 2
                    back_process[i][j] = 3

        process = front_process + [[1, 3]] + back_process
        return process

N = int(input())

result = hanoi_top(N)
print(len(result))
for i in range(2**N-1):
    print(result[i][0], result[i][1])