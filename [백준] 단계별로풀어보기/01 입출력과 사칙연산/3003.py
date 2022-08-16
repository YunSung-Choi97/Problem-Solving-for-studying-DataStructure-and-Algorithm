K, Q, R, B, Kn, P = map(int, input().split())  # 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수
print(1 - K, 1 - Q, 2 - R, 2 - B, 2 - Kn, 8 - P)  # 결과 출력