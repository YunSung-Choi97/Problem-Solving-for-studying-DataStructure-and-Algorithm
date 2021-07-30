N = int(input())
coins = list(map(int, input().split()))
coins.sort()

check_cost = 1
made_cost = []
result = 1
stop = False
find = False

for coin in coins:
    # 현재 화폐보다 적은 금액중 없는 금액 확인
    for i in range(check_cost, coin):
        if not i in made_cost:
            result = i
            stop = True
            break
    if stop:
        find = True
        break

    check_cost = coin
    if len(made_cost) == 0:
        made_cost.append(coin)
    else:    
        temp_list = []
        if not coin in made_cost:
            temp_list.append(coin)
        for i in made_cost:
            if not (i + coin) in made_cost and not (i + coin) in temp_list:
                temp_list.append(i + coin)
        for i in temp_list:
            made_cost.append(i)

if find:
    print(result)
else:
    while True:
        if not check_cost in made_cost:
            print(check_cost)
            break
        check_cost += 1
            