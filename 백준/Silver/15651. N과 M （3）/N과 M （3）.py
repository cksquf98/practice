import sys
input = sys.stdin.readline

def P(depth):
    #종료조건
    if(depth == r):
        for i in range(len(result)):
            print(result[i], end=' ')
        print()
        return

    for i in range(n):
        result[depth] = number[i]
        P(depth+1)


n,r = map(int, input().split())

number = [i for i in range(1,n+1)] #체크리스트 필요 없음!!
result = [0] * r
P(0)