import sys
from collections import deque
input = sys.stdin.readline

# N: 레일에 있는 초밥 개수, d: 초밥의 가짓수, k: 연속 개수, c: 쿠폰
N, d, k, c = map(int, input().split(" "))

sushiList = [int(input()) for _ in range(N)]
sushiList.extend(sushiList[:k-1])

current = []
slide = deque(sushiList[:k])

current = 0

for i in range(k, len(sushiList)):
    kindOfSushi = set(list(slide))

    if c not in kindOfSushi:
        kindOfSushi.add(c)

    current = max(len(kindOfSushi), current)

    slide.popleft()
    slide.append(sushiList[i])

kindOfSushi = set(list(slide))

if c not in kindOfSushi:
    kindOfSushi.add(c)
current = max(len(kindOfSushi), current)

print(current)