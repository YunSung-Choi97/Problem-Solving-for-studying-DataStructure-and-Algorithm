data = input()

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]  # 알파벳 소문자 a ~ z
Alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]  # 알파벳 대문자 A ~ Z

size = len(alphabet)  # 알파벳 소문자 개수
count_Alphabet = [0 for i in range(size)]  # 알파벳의 개수를 저장하는 리스트

# 알파벳 개수 확인
for i in range(size):
    count_Alphabet[i] += data.count(alphabet[i])
    count_Alphabet[i] += data.count(Alphabet[i])

# 알파벳 개수가 최대인 알파벳이 오직 하나인지 확인 후 출력
if count_Alphabet.count(max(count_Alphabet)) == 1:
    print(Alphabet[count_Alphabet.index(max(count_Alphabet))])
else:
    print('?')