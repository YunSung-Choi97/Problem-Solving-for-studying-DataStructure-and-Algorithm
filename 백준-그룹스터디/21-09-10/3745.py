# LIS (Longest Increasing Sequence) : 가장 긴 증가하는 부분 수열
# https://prod.velog.io/@yanghl98/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-LIS-Longest-Increasing-Sequence
# DP방식은 시간초과가 예상되어 Lower Bound방식으로 해결
# 14003번 문제가 길이가 아닌 부분수열을 해결하는 문제

def binary_search(target):  # Index 찾기
    if len(ans) == 0:
        return -1
    
    start_idx = 0
    end_idx = len(ans)-1

    if ans[end_idx] < target:
        return -1
    elif ans[start_idx] > target:
        return 0

    while start_idx <= end_idx:
        if ans[start_idx] > target:
            return start_idx
        elif ans[end_idx] < target:
            break

        mid_idx = (start_idx + end_idx) // 2
        if ans[mid_idx] == target:
            return mid_idx
        elif ans[mid_idx] < target:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx
    
    if end_idx == len(ans)-1 and ans[end_idx] < target:
        return -1
    else:
        return end_idx

while True:
    try:
        N = int(input())
        p = list(map(int, input().split()))

        ans = []

        for i in range(len(p)):
            idx = binary_search(p[i])
            if idx == -1:
                ans.append(p[i])
            else:
                ans[idx] = p[i]

        print(len(ans))
    except:
        break