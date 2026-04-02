# min()함수 사용
N, M = map(int, input().split())

result = 0
for i in range(N):
    number = list(map(int, input().split()))
    min_number = min(number)
    result = max(result, min_number)

print(result)

# 이중 for문 사용
# N, M = map(int, input().split())
#
# result = 0
# for i in range(N):
#     number = list(map(int, input().split()))
#     min_number = 10001
#
#     for a in number:
#         min_number = min(min_number, a)
#
#     result = max(result, min_number)
#
# print(result)