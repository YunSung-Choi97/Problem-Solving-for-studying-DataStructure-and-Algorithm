S = input()
alphabets = 'abcdefghijklmnopqrstuvwxyz'  # 'a' ~ 'z' 순서대로 저장

for char in alphabets:
    print(S.find(char), end=' ')  # find()를 이용해 알파벳의 첫번째 위치를 찾아내고, 만약 없다면 -1을 반환. <-> index()를 이용할 경우 없을때 ValueError 발생.