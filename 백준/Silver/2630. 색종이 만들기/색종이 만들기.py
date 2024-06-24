#시작점을 잡는게 포인트 = (0,0) -> 다음 시작점 : +나눠진 크기
#n/2로 나눠서 재귀적으로 호출했을때 다 1로 이루어져있으면 stop
#크기가 1인 사각형도 색종이 수에 포함됨ㅇㅇ
#하얀색 0, 파란색 1 
def divide(row, col, length):
    global colorCnt
    
    #다른색이 있으면 분할해야함 
    # -> 덧셈 연산을 사용해서 다른 색으로 이루어져있는지 확인
    sum = 0
    for i in range(row, row+length):
        for j in range(col, col+length):
            sum += arr[i][j] #sum이 0(=하얀색) 또는 length*length개(=파란색)
    
    if(sum == 0):
        colorCnt[0] += 1
        return 
    elif(sum == length*length):
        colorCnt[1] += 1
        return
    
    #다른색이 있음 => 분할
    new_length = length//2
    
    top_left =    divide(row,              col,              new_length)
    bottom_left = divide(row + new_length, col,              new_length)
    
    top_right = divide(row,                col + new_length, new_length)
    top_bottom = divide(row + new_length,  col + new_length, new_length)
    
    # if(top_left == bottom_left == top_right == top_bottom == 0):   
    #      colorCnt[0] += 1


if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    colorCnt = [0,0]
    
    divide(0,0,N)
    print(colorCnt[0])
    print(colorCnt[1])