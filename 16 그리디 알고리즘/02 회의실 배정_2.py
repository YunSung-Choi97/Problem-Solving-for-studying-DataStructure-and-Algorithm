# 시간초과 발생
import sys
input = sys.stdin.readline

N = int(input())
time_table = []
for i in range(N):
    time_table.append(list(map(int, input().split())))

start_sorted = sorted(time_table, key = lambda times : times[0])
end_sorted = sorted(time_table, key = lambda times : times[1])

result = 0
while True:
    end_time = end_sorted[0][1]
    
    delete_time = []
    count = 0
    for start_time in start_sorted:
        if start_time[0] < end_time:
            delete_time.append(start_time)
        elif start_time[0] == end_time:
            delete_time.append(start_time)
            count += 1
        else:
            break
    
    if count == 0:
        result += 1
    elif count < len(delete_time):
        result += (1 + count)
    else:
        result += count
    
    for del_time in delete_time:
        start_sorted.remove(del_time)
        end_sorted.remove(del_time)
    
    if len(end_sorted) == 0:
        break

print(result)