N = int(input())
numbers = input()

result = 0
# 문자형으로 받아온 숫자정보를 한 글자씩 읽어 정수형으로 바꿔 더해줌으로서 각자릿수의 합을 계산
for number in numbers:
    result += int(number)
print(result)