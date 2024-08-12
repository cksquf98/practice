import sys
from itertools import combinations 
input = sys.stdin.readline

#n : 동전 화폐 개수, k : 만들려는 동전 총합
n, k = map(int, input().rstrip().split())

coins = list(int(input().rstrip()) for _ in range(n))

dp = [0] * (k+1)

for coin in sorted(coins):
    for i in range(coin,k+1):
        #print(f"{i} >>>>>")
        if(i == coin):
            # print(f"    i={coin} => {dp}")
            dp[i] += 1
        else:
            dp[i] += dp[i-coin]
            # print(f"    i!=coin => {dp}")
            
print(dp[k])