import sys

dic = {}

N = int(sys.stdin.readline())
for i in range(N):
    name, record = sys.stdin.readline().split()
    if(record == 'enter'):
        dic[name]=0
    if(record == 'leave'):
        dic[name]=1


for name, val in sorted(dic.items(), reverse=True):
    if(val == 0):
        print(name)