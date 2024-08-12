import sys
from itertools import combinations 
input = sys.stdin.readline

#n : 동전 화폐 개수, k : 만들려는 동전 총합
n, k = map(int, input().rstrip().split())

coins = list(int(input().rstrip()) for _ in range(n))

dp = [0] * (k+1)

"""
동전 : 1,2,5원
10원을 만드는 경우의 수

1원 : 1 <<1로 나뉘는 애
2원 : 1+1, 2 <<1로 나뉘고 2로도 나뉨
3원 : 1+1+1, 1+2
4원 : 1+1+1+1, 1+1+2, 2+2   <<1,2로 나뉨 : dp[1] + dp[2]
5원 : 1+1+1+1+1, 1+1+1+2, 1+2+2, 5 
6원 : 1+1+1+1+1+1, 1+1+1+1+2, 1+1+2+2, 1+5, 2+2+2
7원 : 1+1+1+1+1+1+1, 1+1+1+1+1+2, 1+1+1+2+2, 1+1+5, 1+2+2+2, 2+5



만약에 동전이 2원, 3원, 5원이고 10원을 만드려고 한다면?

1원 : X
2원 : 2
3원 : 3
4원 : 2+2
5원 : 5, 2+3
6원 : 2+2+2, 3+3
7원 : 5+2
8원 : 2+2+2+2, 3+3+2, 2+3+3, 5+3, 3+5
9원 : 5+2+2, 3+3+3
10원 : 5+5, 2+2+2+2+2, 3+3+2+2+2+2
"""
dp[0] = 1
for coin in sorted(coins):
    for i in range(coin,k+1): #이게 coin부터라는데
        # print(f"{i} >>>>>")
        if(i == coin):
            # print(f"    i={coin} => {dp}")
            dp[i] += 1
        else:
            dp[i] += dp[i-coin]
            # print(f"    i!=coin => {dp}")
            

print(dp[k])