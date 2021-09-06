import sys

data = sys.stdin.readline().rstrip()

if data.count(data[0]) == len(data):  # 문자열 전체가 같은 문자인 경우
    print(-1)
    sys.exit()

for i in range(len(data)-1):
    # 부분문자열의 크기 : len(data) - i
    for start_idx in range(i+1):
        # 부분문자열 시작위치 : start_idx (0 ~ i+1)
        sub_data = data[start_idx:start_idx+len(data)-i]

        for idx in range(len(sub_data)//2+1):  # 회문이 아닌지 확인. 회문이 아닌 경우 부분문자열 출력 후 종료
            if sub_data[idx] != sub_data[-1-idx]:
                print(len(sub_data))
                sys.exit()

# 이것은 문자열 전체가 같은 문자가 아닐 경우 발생하지 않는다. (위 조건 제거 후 이 구문을 통해 동작 시 시간초과)
# print(-1)  # 회문이 아닌 것을 발견하지 못한 경우.