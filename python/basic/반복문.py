for i in range(1,31,10):
    print(f'{i},{i+9}')

dict={1:'first',2:'second',3:'third',4:'fourth', 5:'fifth'}
for i in dict.values():
    print(i)

for k,v in dict.items():
    print(k,v)



i=1
while(i):
    print(i)
    i+=1
    if(i==6):
        break
print(f"{i}에서 끝")


for i in dict.values():
    if(i == 'third'):
        continue
    print(f"{i} complete")
    


#list comprehension = [ 변수 활용형 for 변수 in 반복대상 if 조건 ]
list=[str(x)+'번째' for x in dict.keys() if x%2==0 ] 
print(list)

list2=[x.upper() for x in dict.values() if x.startswith('f')]
print(list2)

list3=[x*2 for x in range(10) if x%2==1]
print(list3)


# 문자열도 for문으로 돌릴 수 있어
for char in input('write down sentence : '):
    print(f'Letter : {char}')


# 문자열.count(문자) : 문자열 내 각 문자에 대한 빈도수를 카운트
s = 'americano joajoajoa'
for char in s:
    print(f'{char} : ',s.count(char))