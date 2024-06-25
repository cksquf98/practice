#퀸 : 자기 주변 모든 방향 일직선
#퀸 자리를 i,j라고 했을 때 i행, j열, (i+n,j+n), (i-n, j-n), (i+n, j-n), (i-n,j+n) 싹 얘네는 배치되면 안됨
    

#자리 체크
def Available(row, col):
    for i in range(row):
        # print(chesspan)
        #i == 행
        #chesspan[i] ==  퀸이 배치된 열 == q_col
        # if(chesspan[i] != -1): #행
        #     print("행 겹침")
        #     return False  --> 아 이 부분이 틀렸던거였음 첨에 무조건 -1로 초기화되어있응께
        
        if(col == chesspan[i]): #열
            # print("열 겹침")
            return False
    
        #대각선 -> 증감 숫자가 동일
        if(abs(i-row) == abs(chesspan[i]-col)):
            # print("대각선")
            return False
    return True    

#가능한 자리 후보를 선택하는 함수 <- 백트래킹
#행 순회하는 for문을 재귀적으로 만들고 열 순회하는 반복문을 수행하도록
def DFS(row):
    global count
    #종료조건 : N행까지 다 돌면서 퀸 배치한 경우
    if(row == N):
        count += 1
        return
    else:
        for col in range(N):
            if(Available(row,col)):
                #배치 가능
                chesspan[row] = col
                
                DFS(row+1)
                
                #돌아온 경우 원상복귀
                chesspan[row] = -1 
                
    
            
            

if __name__ =="__main__":
    import sys
    input = sys.stdin.readline
    
    N = int(input())
    
    chesspan = [-1 for _ in range(N)]   
    #퀸을 배치할 수 있으면 chesspan[row] = col 상태로 저장 
    # -> 난 이걸 첨에 2차원 배열로 해서 for문이 2번 나온건데
    #    이렇게 하니까 for문이 하나면 됨
    
    count = 0 #놓을 수 있는 퀸의 개수
    DFS(0)
    print(count)