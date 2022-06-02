import sys
input = sys.stdin.readline

num_data = []  # 입력받은 숫자들을 저장
num_count = [0 for i in range(-4000, 4001)]  # 입력받은 수의 개수 파악

N = int(input())
for _ in range(N):
    num = int(input())
    num_data.append(num)
    num_count[num+4000] += 1
num_data.sort()

ans1 = sum(num_data) / N
ans2 = num_data[N//2]
if num_count.count(max(num_count)) == 1:  # 개수의 최대값이 하나인 경우
    ans3 = num_count.index(max(num_count)) - 4000
else:  # 개수가 최대값이 하나가 아닌 경우
    ans3 = num_count.index(max(num_count), num_count.index(max(num_count))+1) - 4000  # 개수가 최대인 값들 중 첫번째 인덱스 다음값부터 탐색
ans4 = num_data[-1] - num_data[0]  # 최대값 - 최소값

if -0.5 <= ans1 < 0:  # 산술평균 계산 결과가 해당 범위일 경우 -0이 정답으로 출력되는 것 방지
    ans1 = 0
print('{:.0f}\n{}\n{}\n{}'.format(ans1, ans2, ans3, ans4))  # {:.0f를 이용해 소수점 0자리 표현}