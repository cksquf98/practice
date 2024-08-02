#3스트라이크가 되면 게임이 끝난다

import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline




#입력값
#지금까지 질문한 개수와 질문에 대한 답
Q = int(input())


#가능한 모든 세자리 수 저장
num = deque()
for perm in permutations(["1","2","3","4","5","6","7","8","9"],3):
    # print(perm)
    num.append(perm)

for i in range(Q):
    ans, strike, ball = input().rstrip().split()
    strike = int(strike)
    ball = int(ball)

    
    #답일 가능성이 있는 수 저장
    possibleNum = set()

    
    #perm이 영수가 생각한 답이라고 가정하고 ans에 대한 답을 도출해보는거임    
    for perm in num:
        strikeCheck = 0
        ballCheck = 0
        
        # print(f"perm = {perm}")
        
        for i in range(3):
            #strike 체크
            if(ans[i] == perm[i]):
                strikeCheck += 1

            #ball 체크
            elif(perm[i] in ans):
                ballCheck += 1
        # print(strikeCheck, ballCheck, end=" ")

        if(strike == strikeCheck and ball == ballCheck):
            possibleNum.add(perm)

    num = possibleNum
            
print(len(num))