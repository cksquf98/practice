from itertools import combinations
import sys
input = sys.stdin.readline

height_list = [int(input()) for _ in range(9)]

for com in combinations(height_list, 7):
    sum = 0
    for height in com:
        sum += height

    if(sum == 100):
        for i in sorted(list(com)):
            print(i)

        break