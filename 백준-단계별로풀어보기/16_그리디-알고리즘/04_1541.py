import sys
input = sys.stdin.readline

data = input()

number = []  # 입력받은 숫자들을 저장할 리스트
sign = []    # 입력받은 '+', '-' 연산자를 저장할 리스트
temp = ''    # 최종 결과를 계산하는 과정에서 발생하는 중간 계산값을 저장

# '-'가 나온 이후의 괄호로 묶을 수 있기 때문에 모든 값을 음수로 처리
for value in data:
    if value != '+' and value != '-':
        temp += value
    elif value == '+':
        sign.append(1)
        number.append(int(temp))
        temp = ''
    else:
        sign.append(-1)
        number.append(int(temp))
        temp = ''
number.append(int(temp))

if not -1 in sign:
    print(sum(number))
else:
    idx = sign.index(-1)
    print(sum(number[:idx+1]) - sum(number[idx+1:]))