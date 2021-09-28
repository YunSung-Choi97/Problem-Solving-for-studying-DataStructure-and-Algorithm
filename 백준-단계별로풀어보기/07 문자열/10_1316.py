N = int(input())

result = N
for i in range(N):
    data = input()

    alphabet = []  # data에서 앞 글자부터 한 글자씩 안에 넣어준 뒤 같은 글자가 들어오는지 확인
    check = data[0]  # 확인해야하는 현재글자

    for j in data:
        if j != check:
            if j in alphabet:  # 중복된 글자가 있다면 결과에서 -1
                result -= 1
                break
            alphabet.append(check)
            check = j

print(result)