N, M = map(int, input().split())

results = list()  # 출력할 전체 결과
result = list()  # 출력할 각각의 결과
temp = list()  # 결과를 만들기 위한 임시 리스트
end_condition = [i for i in range(N-M+1, N+1)]  # 탐색 종료 조건

i = 1
while True:
    if len(temp) != M:
        temp.append(i)
        if len(temp) != M:
            i += 1
    else:
        result = temp.copy()
        if result == end_condition:
            results.append(result)
            break
        results.append(result)
        for j in range(M):
            last = temp.pop()
            if last != N-j:
                i = last+1
                break

for i in range(len(results)):
    print(*results[i])