import sys

dic = {}
N,M = map(int,sys.stdin.readline().split())
for i in range(N):
    str = sys.stdin.readline()
    dic[str] = i


count = 0
for j in range(M):
    str = sys.stdin.readline()
    if(dic.get(str)!= None):
        count += 1

print(count)