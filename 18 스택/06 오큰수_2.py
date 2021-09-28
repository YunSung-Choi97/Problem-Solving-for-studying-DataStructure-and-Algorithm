# stack 방식을 이용하지않고 단순 반복문과 조건문으로 구성한 경우.
# 주어진 문제 상황이 N < 1,000,000으로 이와 같은 상황에서는 RunTimeError가 발생할 수 있음. 또한 비효율적이다.

N = int(input())  # N : 수열 A의 크기
A_sequence = list(map(int, input().split()))  # A_sequence : 수열 A를 입력받음
result = []  # result : 결과로 출력할 NGE 수열

for idx, val in enumerate(A_sequence):  # 수열 A의 인덱스와 값을 전달하여 반복

    while idx != N-1:  # 마지막 인덱스값을 제외한 수열 A에 대하여 수행

        idx += 1  # 현재 인덱스값 다음부터 검사를 진행

        # 오큰수 발견
        if val < A_sequence[idx]:
            result.append(A_sequence[idx])
            break
        
        # 오큰수 없음
        if idx == N-1:
            result.append(-1)
            break

result.append(-1)  # 마지막 인덱스값은 오큰수가 존재할 수 없기때문에 모든 상황에서 -1

# [결과출력] result 값들을 출력
for i in range(N):
    print(result[i], end = ' ')