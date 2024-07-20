import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque()

for i in range(1,N+1):
    deque.append(queue, i)

print('<', end='')
while len(queue) > 1:
    for _ in range(K-1):
        deque.append(queue, deque.popleft(queue))

    print(deque.popleft(queue), end=', ')

print(deque.popleft(queue), end='>')