import sys
input = sys.stdin.readline


def P(index):
    if(index == r):
        for l in range(len(result)):
            print(result[l], end=' ')
        print()
        return
    for i in range(n):
        if(checklist[i] == False):

            result[index] = number[i] #첨 뽑은 애를 result r자리에 저장
            checklist[i] = True
            
            P(index+1)
            #체크리스트 원상복귀
            checklist[i] = False

#수열 : nPr -> n개의 수 중에서 r만큼 뽑는다
n, r = map(int, input().split())
number = [i for i in range(1,n+1)]

#중복없는 수열 -> 체크리스트 필요
checklist = [False]*n

#r개 뽑은 결과리스트
result = [0] * r

P(0)