# quickSort 함수 정의
def quickSort(s, low, high):
    if high > low:
        pivot_idx = partition(s, low, high)
        quickSort(s, low, pivot_idx-1)
        quickSort(s, pivot_idx+1, high)

# partition 함수 정의
def partition(s, low, high):
    global count
    pivot_idx = low
    pivot_item = s[pivot_idx]

    j = low
    for i in range(low+1, high+1):
        count += 1
        if s[i] < pivot_item:
            j += 1
            s[i], s[j] = s[j], s[i]
    pivot_idx = j
    s[low], s[pivot_idx] = s[pivot_idx], s[low]
    return pivot_idx


# Test case 1
# s = [3, 5, 2, 9, 10, 14, 4, 8]
# quickSort(s, 0, 7)

# 난수를 뽑기위해 random 모듈 사용
import random

counts = []  # quick sort로 정렬할 때 평균 데이터 비교 횟수들
for n in [8, 16, 24, 32, 40]:  # 데이터의 개수 n이 8, 16, 24, 32, 40으로 변화
    count = 0  # quick sort로 정렬할 때 데이터 비교 횟수
    data_set = [[random.randint(0, n) for j in range(n)] for i in range(20)]  # 0 ~ n 범위의 난수 n개로 구성된 20개의 데이터셋
    # 모든 데이터셋에 대하여 퀵정렬
    for i in range(20):
        # print('n = {}일때, {}번째 정렬 결과\n{}'.format(n, i+1, data_set[i]))  # 동작 확인
        quickSort(data_set[i], 0, n-1)
        # print(' -> {}\n'.format(data_set[i]))  # 동작 확인
    counts.append(count / 20)

# quick sort로 정렬할 때 평균 데이터 비교 횟수들 확인
for i in range(5):
    print('n = {:2}일 때 평균 데이터 비교 횟수 : {}'.format((i+1)*8, counts[i]))

# 그래프를 그려주기 위해 matplotlib.pyplot 사용
from matplotlib import pyplot as plt

# x축 : 정렬할 데이터의 크기
# y축 : quick sort로 정렬할 때 평균 데이터 비교 횟수
x_data = [8, 16, 24, 32, 40]
y_data = counts

# 축 간격을 8로 설정
plt.xticks(x_data)

# 그래프 그리기 (좌표에 점 표현, 점과 점을 선으로 연결)
plt.plot(x_data, y_data, 'o-')
plt.show()