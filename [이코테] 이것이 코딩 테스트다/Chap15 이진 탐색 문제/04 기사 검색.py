from bisect import bisect_left
from bisect import bisect_right

# 문자열을 뒤집은 후 정렬하여 반환
def sorted_reverse_string(string_list):
    result = string_list.copy()

    # 문자열 뒤집기
    for i in range(len(result)):
        result[i] = result[i][::-1]

    result.sort()  # 정렬

    return result

def solution(words, queries):
    answer = []

    # 가사 단어의 길이에 따라 저장
    words_of_length = [[] for _ in range(10001)]
    for word in words:
        words_of_length[len(word)].append(word)

    # words_of_length_front[i]: 가사 단어의 길이가 i이고 정렬된 리스트
    words_of_length_front = []
    for i in range(10001):
        words_of_length_front.append(sorted(words_of_length[i]))

    # words_of_length_back[i]: 가사 단어의 길이가 i이고, 가사 단어를 뒤집은 후 정렬된 리스트
    words_of_length_back = []
    for i in range(10001):
        words_of_length_back.append(sorted_reverse_string(words_of_length[i]))

    for querie in queries:
        wildcard_location = 'front'  # 와일드카드의 위치 (접두사인지 확인)
        if querie[0] != '?':
            wildcard_location = 'back'
        
        length = len(querie)  # 검색 키워드의 길이

        # 와일드카드가 접두사인 경우
        if wildcard_location == 'front':
            left = bisect_left(words_of_length_back[length], querie[::-1].replace('?', 'a'))
            right = bisect_right(words_of_length_back[length], querie[::-1].replace('?', 'z'))
        # 와일드카드가 접미사인 경우
        else:
            left = bisect_left(words_of_length_front[length], querie.replace('?', 'a'))
            right = bisect_right(words_of_length_front[length], querie.replace('?', 'z'))

        answer.append(right - left)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
''' 입력 예시 1
["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]
'''
''' 출력 예시 1
[3, 2, 4, 1, 0]
'''