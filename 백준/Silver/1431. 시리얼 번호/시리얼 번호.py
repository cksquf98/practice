def sum(str):
    count = 0
    for s in str:
        if(ord(s) >= 65):
            continue
        else:
            count += int(s)
    
    return count


import sys
input = sys.stdin.readline

N = int(input())
serial = list(input().rstrip() for _ in range(N))

serial.sort(key= lambda x : (len(x), sum(x), x))

for elem in serial:
    print(elem)