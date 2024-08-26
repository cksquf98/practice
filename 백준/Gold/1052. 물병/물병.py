from math import log2
import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

if N <= K:
    print(0)
    exit()

current = []

while N:
    num = 2 ** int(log2(N))
    heapq.heappush(current, num)
    N -= num

count = 0

while len(current) > K:
    first = heapq.heappop(current)

    if not current:
        break

    second = current[0]

    if first == second:
        heapq.heappop(current)
        heapq.heappush(current, first + second)
    else:
        # 두 배로 만들기 위해 필요한 추가 물병 수 계산
        count += first
        heapq.heappush(current, first * 2)

print(count)
