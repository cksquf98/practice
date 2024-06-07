import sys

N = int(sys.stdin.readline())

#미리 소수 배열 만들어 놓기
arr = [True] * 1000001
arr[0] = False
arr[1] = False

for i in range(2, int(1000000/2) + 1):
    for j in range(i*2,len(arr), i):
        arr[j] = False



def eratosthenes(num):
    #전역변수 명시해줘야함
    global count
    for k in range(2, int(num/2) + 1):
        if(arr[k] == True and arr[num-k] == True):
            count += 1


for i in range(N):
    num = int(sys.stdin.readline())
    count = 0
    eratosthenes(num)
    print(count)