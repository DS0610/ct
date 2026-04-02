N, K = map(int, input().split())

count = 0
while True:
    result = (N // K) * K
    count += (N - result)
    N = result

    if N < K:
        break

    count += 1
    N //= K

count += (N - 1)
print(count)