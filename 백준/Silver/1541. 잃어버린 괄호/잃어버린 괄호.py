# - 뒤에 +가 오면 + 연산자 이어지는 곳까지 쫙 괄호로 묶으면 될라남?

import sys
input = sys.stdin.readline

exp = input().rstrip().split("-")


ans = 0

for i in range(len(exp)):
    if(i==0 and "+" not in exp[i]):
        ans += int(exp[i])
        
    elif(i==0 and "+" in exp[i]):
        ans += sum(map(int, exp[i].split("+")))

    elif(i>0 and "+" in exp[i]):
        ans -= sum(map(int, exp[i].split("+")))
    else:
        ans -= int(exp[i])

print(ans)