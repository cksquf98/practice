# -_-......................................
if __name__=="__main__":
    import sys
    input = sys.stdin.readline

    DP = [[0,0,0] for _ in range(100000)]
    N = int(input())
    
    DP[0][0] = 1
    DP[0][1] = 1
    DP[0][2] = 1

    for i in range(1,100000):
        DP[i][0] = (DP[i-1][0] + DP[i-1][1] + DP[i-1][2]) % 9901
        DP[i][1] = (DP[i-1][0] + DP[i-1][2]) % 9901
        DP[i][2] = (DP[i-1][0] + DP[i-1][1])%9901

    print((DP[N-1][0]+DP[N-1][1]+DP[N-1][2])%9901)