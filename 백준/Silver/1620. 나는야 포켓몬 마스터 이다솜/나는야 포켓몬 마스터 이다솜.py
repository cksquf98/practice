import sys

words, question = map(int,sys.stdin.readline().split())
dic = {}

for i in range(1,words+1):
    pokemon = sys.stdin.readline().strip()
    dic[i] = pokemon
    dic[pokemon] = i

for j in range(question):
    q = sys.stdin.readline().strip()
    if(ord(q[0])-65 >= 0):     # ord() : 문자열을 아스키코드로 반환해주는 함수!!
        print(dic.get(q))
    else:
        q = int(q)
        print(dic.get(q))