num_list=list(range(0,21))
str_list=['a','a','a','b','c','d','e']
tuple1=(1,'a',3,4,'아하~~',3.14)


(a,b,*others)=tuple1 #나머지 리스트 값은 *변수 <<여기로 싹
print(others)

dict={1:'first', 2:'second','third':'세번째'}
dict['1']='firsttt'         #딕셔너리 키:값 추가
dict['third']='samsam'      #값 수정
dict.update({1:'FIRST','1':'FirstT'})   #여러개 값 수정
print(dict)

# 리스트 > 딕셔너리 > 리스트
listToDict=dict.fromkeys(str_list) #중복 제거된 리스트 값을 키로 만듬
print(listToDict)
dictToList=list(listToDict) #key값을 뽑아서 리스트로 저장
print(dictToList)


# 리스트 참조와 복사 차이
x = [1,2,3,4,5]
y = x       # 같은 리스트를 참조하는 x,y
x[0] = 10
print(y)    # 값 바뀌어 있음

y = x[:]    # 슬라이싱 >> 리스트 복사본이 할당됨
x[0] = 100
print(y)    # 값 그대로


# 리스트 연결 : extend()
x.extend(y)
print(x)


# 리스트 값 제거 : pop(인덱스), remove(값)
print(x.pop(0))
print(y.remove(10))