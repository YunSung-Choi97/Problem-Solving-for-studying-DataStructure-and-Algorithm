data = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

result = len(data)
for croatia_alp in croatia:
    result -= data.count(croatia_alp)  # 두 글자가 한 문자이므로 하나로 셀 수 있도록 개수마다 1씩 빼줌

# 'dz='에 대하여 -2를 해야하지만 'dz=' 하나 당 'z='이 하나 세어지기 때문에 뺄 필요가 없다
print(result)