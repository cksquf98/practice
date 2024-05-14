from math import sqrt
import sys



def findPrime(num):
    
    #sq = int(sqrt(num)) 여기에서 sq 값 설정하면 에러 -> 24 넣었을 때 25나옴
    #+1된 num에 맞게 제곱근 설정되어야 하는걸 놓침
    while(1):
        sq = int(sqrt(num))
        flag = True
        for i in range(2, sq+1):  
            if(num % i == 0):
                flag = False
                break

        if (flag):
            return num
        
        num += 1
    
    return num

N = int(sys.stdin.readline())
for k in range(N):
    num = int(sys.stdin.readline())
    if(num <= 2):    print(2)
    else:
        print(findPrime(num))
