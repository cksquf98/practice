import sys


s = set()
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

dic = {}
for i in range(len(cards)):
    dic[cards[i]] = 1


M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))


for checkCard in checks:
    flag = dic.get(checkCard)
    if(flag):
        print(1, end = ' ')
    else:
        print(0, end = ' ')