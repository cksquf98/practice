# Y = 2명이서 하는 게임
# F = 3명이서 하는 게임
# O = 4명이서 하는 게임

import sys
input = sys.stdin.readline

N, game = input().rstrip().split(' ')

gamePlayer = 0
if game == 'Y':
    gamePlayer = 1
elif game == 'F':
    gamePlayer = 2
elif game == 'O':
    gamePlayer = 3

player = set([input().rstrip() for i in range(int(N))])

print(len(player) // gamePlayer)