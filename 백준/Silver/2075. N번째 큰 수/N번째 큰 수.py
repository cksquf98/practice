import sys
import heapq
input = sys.stdin.readline

N = int(input())

candidate = list(map(int, input().split(" ")))
heapq.heapify(candidate)

for i in range(N-1):
    inputList = list(map(int, input().split(" ")))

    for element in inputList:
        if element > candidate[0]:
            heapq.heappop(candidate)
            heapq.heappush(candidate, element)

print(candidate[0])