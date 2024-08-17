import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    real = {}
    for num in list(map(int, input().split())):
        real[num] = True
    
    M = int(input())
    insist = list(map(int, input().split()))

    # print(real)
    # print(insist)

    
    for i in insist:
        if(real.get(i) != None):
            print(1)
        else:
            print(0)
