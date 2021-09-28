N = int(input())
have_item = list(map(int, input().split()))
M = int(input())
find_item = list(map(int, input().split()))

for item in find_item:
    if item in have_item:
        print('yes', end=' ')
    else:
        print('no', end=' ')