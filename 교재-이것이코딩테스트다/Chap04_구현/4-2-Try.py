start_point = input()

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y = ['1', '2', '3', '4', '5', '6', '7', '8']

x_point = x.index(start_point[0])
y_point = y.index(start_point[1])

result = 8
if x_point < 2 or x_point > 5:
    result -= 2
if y_point < 2 or y_point > 5:
    result -= 2

print(result)