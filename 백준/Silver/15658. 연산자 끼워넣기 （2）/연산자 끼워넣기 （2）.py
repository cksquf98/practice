def DFS(depth, current, plus, minus, mul, div):
    global min
    global max

    #종료조건 -> 숫자 다 돌았을 때
    if(depth == N):
        if(current > max):
            max = current
        if(current < min):
            min = current
        
        return

    if plus:
        DFS(depth+1, current+number[depth], plus-1, minus, mul, div)
    
    if minus:
        DFS(depth+1, current-number[depth], plus, minus-1, mul, div)

    if mul:
        DFS(depth+1, current*number[depth], plus, minus, mul-1, div)
    
    if div:
        #음수 나누기 : 파이썬은 -3/2의 결과이 -1.5인 경우 소수점 아래의 수를 '올림'한다. 따라서 '-3//2'의 연산값은 -2가 된다.
        DFS(depth+1, int(current/number[depth]), plus, minus, mul, div-1)

if __name__=="__main__":
    import sys
    from itertools import permutations
    input = sys.stdin.readline

    N = int(input())

    number = list(map(int,input().split()))

    plus, minus, mul, div = map(int, input().split())

    min= float('inf')
    max= -float('inf')

    current = number[0]
    DFS(1, current, plus, minus, mul, div)

    print(max)
    print(min)