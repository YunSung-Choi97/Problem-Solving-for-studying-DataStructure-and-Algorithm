# 미완.
# 약수로 할 필요가 없음. 뒤에 남는 부분은 붙여서 구현필요.

def solution(s):
    # 전체 길이의 약수 찾기
    len_div = []
    for i in range(1, len(s) // 2 + 1):
        if len(s) % i == 0:
            len_div.append(i)

    results = []
    # 약수마다 문자열 압축
    for div in len_div:
        # 문자열 나누기
        s_div = []
        for i in range(0, len(s), div):
            s_div.append(s[i:i+div])
        
        result = ''
        count = 1
        for i in range(1, len(s_div)):
            if i == len(s_div)-1:
                if s_div[i-1] == s_div[i]:
                    count += 1
                    result += str(count)
                    result += s_div[i-1]
                elif count == 1:
                    result += s_div[i-1] + s_div[i]
                else:
                    result += str(count) + s_div[i-1] + s_div[i]
            
            elif s_div[i-1] == s_div[i]:
                count += 1
            else:
                if count == 1:
                    result += s_div[i-1]
                else:
                    result += str(count) + s_div[i-1]
                    count = 1
        results.append(result)
    print(results)
    answer = len(s)
    for result in results:
        if len(result) < answer:
            answer = len(result)
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))