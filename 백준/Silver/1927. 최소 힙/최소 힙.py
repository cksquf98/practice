import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    if num == 0 and len(heap) > 0:
        print(heapq.heappop(heap))
    elif num == 0 and len(heap) == 0:
        print(0)
    else:
        heapq.heappush(heap, num)