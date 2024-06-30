
if __name__=="__main__":
    import sys
    input = sys.stdin.readline
    n, k = map(int, input().split())

    coins = list(set(int(input()) for _ in range(n)))
    coins.sort(reverse=True)
    
    dp = [float('inf')]*(k+1) #K원을 만들기 위한 최소 동전 수

    # 동전이 1부터 시작하면
    dp[0] = 0
    # dp[1] = 1
    # dp[2] = dp[1]+1
    # dp[3] = dp[2]+1
    # dp[4] = dp[3]+1
    # dp[5] <-- coins에 있음 => dp[4]+1이랑 5원 동전 쓴거랑 비교
 
    
    #큰 동전 쓸 수 있는 금액부터 반복문 돌리면서 개수 갱신
    for coin in coins:
        for i in range(coin, k+1):
            dp[i] = min(dp[i], dp[i-coin]+1)



    # print(dp)
    if(dp[k] == float('inf')):
        print(-1)
    else:
        print(dp[k])