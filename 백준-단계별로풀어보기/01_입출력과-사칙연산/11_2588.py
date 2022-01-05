num1 = int(input())
num2 = int(input())

# 뒤에 수를 원하는 자리를 고려하여 %연산자를 이용해 앞을 자르고, //연산자를 이용해 뒤를 잘라주었다.
print(num1 * (num2%10))
print(num1 * (num2%100//10))
print(num1 * (num2%1000//100))
print(num1 * num2)