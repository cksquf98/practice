import sys

N = int(sys.stdin.readline())
dic = {}
count = 0

for i in range(N):
    s = sys.stdin.readline().strip()
    #sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아짐
    
    if(s == "ENTER"):
        dic = {}
        continue
    else:
        if(dic.get(s) == None):
            dic[s] = 1
            count += 1
print(count)