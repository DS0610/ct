price = int(input())

count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += price // coin # 거슬러 줄 수 있는 동전의 개수
    price %= coin

print(count)