def DFS(index,sum):
    global count
    #가지치기 추가
    if (index == N):
       return
    # if (index == N or sum+numbers[index] > S): 아 숫자 커져도 뒤에 음수 나올 수도 있으니까 이거 안되는 조건이구나
    #     return
    if(S == sum+numbers[index]):
        count += 1
        # return  --> 탐색 계속되어야 하기 떄무넹


    #부분집합을 만들어두는 방식이 아니라
    #이진탐색처럼 <숫자 선택 OR 선택 안함> 여부로 나눠서 재귀돌리기
    #해당 숫자 포함 선택
    DFS(index+1, sum+numbers[index])

    #해당 숫자 미포함 선택
    DFS(index+1, sum)

if __name__=="__main__":
    import sys
    input = sys.stdin.readline

    N, S = map(int, input().split())

    numbers = list(map(int, input().split()))
    
    count = 0
    DFS(0,0)
    print(count)