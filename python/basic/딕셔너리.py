# 딕셔너리 {key : value} : 키는 고유값
dic = {1:'a', 2:'b'}
dic[1]='c'
dic[3]='d'


# 리스트는 key 불가 value 가능
l = [1,2,3]
#dic[l] = 'e' : error!
dic[4] = l
print(dic)


#set 생성 : 되도록 set()를 쓰자
s = {1,2,3} #set
dictionary = {} #dic
print(type(s))

#in 연산 : key에 대해서만 수행
if(1 in dic):
    print("ok")
if('c' in dic):
    print("ok2")


#메소드 get(탐색할 키, 없을 경우 반환할 디폴트값)
print(dic.get('c',"Default"))


#딕셔너리 반복
for key in dic:
    print(key," ",dic[key])


#메소드 items() : 키-값을 튜플로 반환하는데 접근이 안됨 => 반복문으로 접근
pairs = dic.items()
print(pairs)
print(type(pairs))
for key, val in pairs:
    print(key, " ", val)