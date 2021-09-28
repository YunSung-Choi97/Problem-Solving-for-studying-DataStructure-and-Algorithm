'''미리 생각하기
1. 입력받기 (N, An, 연산자 수)
2. 계산하기
 2-1. 첫번째 숫자를 불러옴
 2-2. 사용할 연산자 선택 & 다음 숫자 불러옴 >> 반복하여 N자리 숫자를 모두 불러오면 결과 저장
 2-3. BackTracking으로 연산자를 하나씩 바꿔나감
3. 저장된 결과 중 최대값과 최소값 출력 >> (수정) 많은 결과 중 최대, 최소를 선택하는 것보다는 결과가 정해질 때마다 최대, 최소를 업데이트하는 것이 효율적이라 판단
 : 실제로 메모리와 시간이 개선됨. (수정전) 174540KB / 7936ms, (수정후) 29200KB / 7728ms
'''
# 입력받기
N = int(input())  # N 입력받기
An = list(map(int, input().split()))  # A1, A2, ... , An 입력받기
Bn = list(map(int, input().split()))  # 연산자 수 입력받기

operator = [i for i in range(4) for j in range(Bn[i])]  # 더하기, 빼기, 곱하기, 나누기를 각각 0, 1, 2, 3으로 대응시켜 연산자 수에 맞게 넣어줌
using = [False] * (N-1)  # 연산자가 사용중인지 상태를 표현

# 이전까지의 계산값과 계산할 숫자순서를 입력받고, 모든 자리를 다 계산하면 결과에 추가하는 함수
def calculator(pre_value, k):
    if k == N:
        global max_result, min_result
        if max_result < pre_value:
            max_result = pre_value
        if min_result > pre_value:
            min_result = pre_value
        return

    for i in range(N-1):
        if using[i]:
            continue
        oper = operator[i]
        using[i] = True
        value = calculate(pre_value, An[k], oper)
        calculator(value, k+1)
        using[i] = False

# 연산자에 맞는 계산값 반환
def calculate(num1, num2, oper):
    if oper == 0:
        return num1 + num2
    if oper == 1:
        return num1 - num2
    if oper == 2:
        return num1 * num2
    if oper == 3:
        if num1 >= 0: return num1 // num2
        else: return -((-num1) // num2)

first_value = An[0]
max_result, min_result = int(-1e9), int(1e9)
calculator(first_value, 1)
print('{}\n{}'.format(max_result, min_result))