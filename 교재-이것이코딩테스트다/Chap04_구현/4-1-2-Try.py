N = int(input())

three_in_hour = 9*5*(9+5+9+5) + 9*(5+9+5)+5*(9+5+9) + (9+5+9+5) + 1
hour = 60 * 60

hours = []
result = 0
for i in range(24):
    if i in [3, 13, 23]:
        result += hour
    else:
        result += three_in_hour
    hours.append(result)

print(hours[N])

'''
~ 00 59 59
1) 3이 하나만 들어가는 경우
3X XX : 9x5x9
X3 XX : 5x5x9
XX 3X : 5x9x9
XX X3 : 5x9x5

2) 3이 두개만 들어가는 경우
33 XX : 5x9
3X 3X : 9x9
3X X3 : 9x5
X3 3X : 5x9
X3 X3 : 5x5
XX 33 : 5x9

3) 3이 세개만 들어가는 경우
33 3X : 9
33 X3 : 5
3X 33 : 9
X3 33 : 5

4) 3이 네개만 들어가는 경우
33 33 : 1
'''