'''
"a,e,i,o,u" 모음 뒤 'p'문자 + 해당 모음 다시 추가된 암호화 문장 입력 시
원문 출력하기
'''
txt = input('암호화 문장 입력 :')
origin = ''
i = 0

while(i<len(txt)):
    origin+=txt[i]      # 공통 동작이였구만
    if(txt[i] in "aeiou"):
        # origin+=txt[i]
        i+=3
    elif(txt[i]==' '):
        # origin+=' '
        i+=1
    else:
        # origin +=txt[i]
        i+=1
print(origin)