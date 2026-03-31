N, M, K = map(int, input().split())

list_n = list(map(int, input().split()))
list_n.sort()

first = list_n[-1] # 가장 큰 수
second = list_n[-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수
count = (M // (K + 1)) * K
count += M % (K + 1)

result = 0
result += count * first
result += (M - count) * second

print(result)