import sys
input = sys.stdin.readline

data = input()
alp = []
num = []

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in data[:-1]:
    if i in number:
        num.append(int(i))
    else:
        alp.append(i)

alp.sort()
result = ''
for i in alp:
    result += i
result += str(sum(num))

print(result)