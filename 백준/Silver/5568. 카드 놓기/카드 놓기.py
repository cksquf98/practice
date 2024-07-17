import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
K = int(input())

cards = [0 for _ in range(N)]

for i in range(N):
    cards[i] = int(input())

p = set()

for perm in permutations(cards, K):
    res = ""
    for num in perm:
        res += str(num)
    p.add(res)

print(len(p))