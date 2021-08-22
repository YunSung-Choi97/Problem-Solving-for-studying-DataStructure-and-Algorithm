N, M = map(int, input().split())

num_used = [False for i in range(N+1)]  # num이 사용되었는지 확인하는 리스트
results = list()  # 출력할 전체 결과
result = list()  # 출력할 각각의 결과
temp = list()  # 결과를 만들기 위한 임시 리스트
end_condition = [i for i in range(N, N-M, -1)]  # 탐색 종료 조건

i = 1
while True:
    if len(temp) != M:
        if num_used[i]:
            i += 1
        else:
            temp.append(i)
            num_used[i] = True
            i = 1
    else:
        result = temp.copy()
        if result == end_condition:
            results.append(result)
            break
        results.append(result)
        for j in range(M):
            last = temp.pop()
            if j < num_used[last:].count(False) or j == M-1:
                num_used[last] = False
                i = last+1
                break
            else:
                num_used[last] = False

for i in range(len(results)):
    print(*results[i])