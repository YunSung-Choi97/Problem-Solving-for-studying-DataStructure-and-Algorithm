datas = input()

result = 0
mapping_num_char = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']  # 2 ~ 9까지 숫자를 알파벳에 대응

# 알파벳에 해당하는 숫자(i+2)를 알아내서 1을 더하여 걸리는 시간을 계산
for char in datas:
    for i in range(len(mapping_num_char)):
        if char in mapping_num_char[i]:
            result += i+3
            break

print(result)