def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x : (x[col-1], -x[0]))
    # print("data: ",data)
    
    S_i = []
    for row in range(row_begin-1, row_end):
        cnt = 0
        for elem in data[row]:
            cnt += elem % (row+1)
        S_i.append(cnt)
    
    # print(S_i)
    answer = S_i[0]
    for i in range(1, len(S_i)):
        answer = answer ^ S_i[i]
        
    
    return answer