N = 1260

coins = [500, 100, 50, 10]
result = 0

for coin in coins:
    if N >= coin:
        count = N // coin
        result += count
        N %= coin

print(result)