import sys
input = sys.stdin.readline

N = int(input())
number = list(map(int, input().split()))

add,minus,multi,div = map(int, input().split())

result = []

def operator(add, minus, multi, div, total, numberIndex):
    if(add == 0 and minus == 0 and multi == 0 and div == 0):
        result.append(total)
        return
    
    if(add > 0):
        # total += number[numberIndex]이케 해버리면 total값이 아예 저장이 되어버려서 이상하게 변경됨
        operator(add-1, minus, multi, div, total+number[numberIndex], numberIndex+1)
    
    if(minus > 0):
        operator(add, minus-1, multi, div, total-number[numberIndex], numberIndex+1)

    if(multi > 0):
        operator(add, minus, multi-1, div, total*number[numberIndex], numberIndex+1)
    
    if(div > 0):
        #total이 음수면 (-total)/num
        if(total < 0):
            operator(add, minus, multi, div-1, -((-total)//number[numberIndex]), numberIndex+1)
        else:
            operator(add, minus, multi, div-1, total//number[numberIndex], numberIndex+1)


#첫번째 원소를 total에 넣고 시작
operator(add, minus, multi, div, number[0], 1)


#최댓값 최솟값 출력
# print(result)
print(max(result))
print(min(result))