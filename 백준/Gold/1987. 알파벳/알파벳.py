def Available(row, col, used_alphabet):
    if(col >= C or col < 0):
        return False
    elif(row >= R or row < 0):
        return False
    elif(roadmap[row][col] in used_alphabet):
       return False
    return True

def DFS(row, col, used_alphabet, count):
    global max_count

    alpha = roadmap[row][col]
    used_alphabet[alpha] = True

    #상
    if(Available(row-1,col,used_alphabet)):
        DFS(row-1, col,used_alphabet, count+1)
    
    #하
    if(Available(row+1, col, used_alphabet)):
        DFS(row+1, col, used_alphabet, count+1)

    #좌
    if(Available(row,col-1,used_alphabet)):
        DFS(row, col-1,used_alphabet, count+1)

    #우
    if(Available(row,col+1,used_alphabet)):
        DFS(row, col+1,used_alphabet, count+1)

    ### 상하좌우 이동 못하면 원상복구해주고 돌아가야함
    used_alphabet.pop(alpha)
    max_count = max(max_count, count)
    return


if __name__=="__main__":
    import sys
    input = sys.stdin.readline

    R,C = map(int, input().split())
    
    roadmap = [[char for char in input().rstrip()] for _ in range(R)]

    max_count = 0
    DFS(0,0,{},1)
    print(max_count)