N = int(input())  # N : 수열 A의 크기
A_sequence = list(map(int, input().split()))  # A_sequence : 수열 A를 입력받음
stack = []  # stack : 수열 A의 인덱스를 차례로 push받고, 더 큰 값을 만났을 때 pop 처리됨
result = [-1 for _ in range(N)]  # result : 결과로 출력할 NGE 수열

for i in range(N):  # N번 반복

    try:  # stack이 비어있는 경우에는 IndexError가 발생. pass처리한 후 stack에 현재 인덱스를 추가.
        while A_sequence[stack[-1]] < A_sequence[i]:  # stack 안에 있는 값(인덱스)들에 대해 수열에서 현재값보다 작은지 확인
            result[stack.pop()] = A_sequence[i]  # 현재값보다 작은 경우 result[인덱스]에 현재값 할당
    except:
        pass
        
    stack.append(i)

# [결과출력] result 값들을 출력
for i in range(N):
    print(result[i], end = ' ')