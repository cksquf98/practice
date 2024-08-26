from math import log2
import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

if(N <= K):
    print(0)
    exit()

current = []

while N:
    num = 2 ** int(log2(N))
    heapq.heappush(current, num)
    N -= num

# print(current)
count = 0

while len(current) > K :
    first = heapq.heappop(current)

    if(not current):
        break

    second = current[0]


    if(first == second):
        heapq.heappop(current)
        heapq.heappush(current, first + second)
    else:
        count += second - first
        heapq.heappop(current)
        heapq.heappush(current, second *2)

if count == 0:
    print(0)
else:
    print(count)