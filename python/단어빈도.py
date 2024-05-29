'''
m개의 단어가 주어질 때, 출현 빈도가 k번째로 높은 단어를 찾아라
k=1 : 가장 빈도 높음, 위에 아무도 없음
k=2 : 빈도 높은 단어가 위에 한개 있음
k=3 : 빈도 높은 단어가 위에 두개 있음

input : 
1. m k
2. 단어 m개 줄단위 입력

output : 
1. K번째 빈도 높은 단어는
2. 단어 나열
3. (\n)
'''
m,k = map(int,input('단어의 개수 및 빈도수를 입력하시오').split())
dic = {}
for i in range(m):
    word = input('단어 입력 : ')
    
    #이미 딕셔너리에 있으면 +1
    if(word in dic):
        dic[word] += 1
    else:   #없으면 생성
        dic[word] = 1
        #근데 이렇게 하면 빈도 수로 단어를 일일이 찾기 힘듬 => 횟수를 키로 만들자 inverKeyValue


def invertKeyValue(dic):
    invert = {}
    for word in dic:
        counts = dic[word]                  #빈도 수 value를 counts에 저장 
        if(counts in invert):               #딕셔너리에 있는 빈도 수였으면 단어 리스트에 추가
            invert[counts].append(word)
        else:
            invert[counts] = list()         #주의: list('ab') -> ['a','b']이렇게 만들어짐
            invert[counts].append(word)
    return invert


invertedDic = invertKeyValue(dic)
invertedDic = sorted(invertedDic.items(),reverse=True)


# K번째 빈도수 찾기: 자신보다 빈도가 높은 단어가 k-1개면, 해당 단어는 k번째 빈도수를 가짐
count = 0
for key,val in invertedDic:
    if(count == k-1):
        print(f'{k}번째 빈도 높은 단어는')
        for v in val:
            print(v)
        break
    elif(count > k-1):
        print(f"{k}번째 빈도수를 가진 단어는 없습니다.")
        break
    else:
        count += len(val)