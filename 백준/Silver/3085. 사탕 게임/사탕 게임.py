#와 이거 머냐 대박 무식 반복문이였네 ㅡ.ㅡ 몰겠어서 찾아봄
def lenCheck():
    global maxCnt

    for i in range(N):
        #행 검사
        row_cnt = 1
        for j in range(1,N):
            if(map[i][j-1] == map[i][j]):
                row_cnt += 1
                maxCnt = max(row_cnt, maxCnt)
            else:
                row_cnt = 1

        #열 검사
        col_cnt = 1
        for j in range(1,N):
            if(map[j][i] == map[j-1][i]):
                col_cnt += 1
                maxCnt = max(maxCnt, col_cnt)
            else:
                col_cnt = 1



if __name__=="__main__":
    import sys
    input = sys.stdin.readline
    N = int(input())
    map = [[char for char in input().rstrip()] for _ in range(N)]
    
    maxCnt = 0
    
    #Swap - 고른 칸에 들어있는 사탕과 다음 열/ 다음 행 서로 교환해가면서 최대 길이 체크
    for i in range(N):
        for j in range(N):
            #상/하/우 체크하는게 아니라 우/하만 체크하면 됨!!
            #왜냐면 첫번째 줄 하 = 두번째줄 상 이기 때무넹 

            #오른쪽 체크
            if(j+1 < N):
                map[i][j], map[i][j+1] = map[i][j+1], map[i][j]
                lenCheck()
                #바꾼거 원상복구
                map[i][j], map[i][j+1] = map[i][j+1], map[i][j]

            #아래 체크
            if(i+1 < N):    
                map[i][j], map[i+1][j] = map[i+1][j], map[i][j]
                lenCheck()
                #바꾼거 원상복구
                map[i][j], map[i+1][j] = map[i+1][j], map[i][j]

    print(maxCnt)