# 파일 쓰기 모드
file=open('file.txt','w',encoding='utf-8')
file.write('hahahahaha\n')
file.write('hohohohoho\n')
file.close()

# 쓰기 모드2
output_file = open('python/out.in','w',encoding='utf-8')
output_file.write('hi')
output_file.write('배가 고픈거가태')
num = 882
output_file.write(num) # 파일엔 string만 쓸 수 있음
output_file.write(str(num)) 
output_file.close()

# with구문 : file.close() 안써도 됨
with open('file.txt', 'w',encoding='utf-8') as file3:
    file3.write('12345678')

# 파일 읽기 모드
file2=open('file.txt','r',encoding='utf-8')   
content=file2.read()
#print(content)
for line in content:
    print(line,end='...')
file2.close()

# 읽기 모드2
file = open('python/word.in','r',encoding='utf-8')
print(file.readline())              # readline(): 각 줄 string 반환, \n 같이 출력됨, 다 읽어졌으면 빈 문자열 출력
print(file.readline().rstrip())     # rstrip(): 문자열 오른쪽 공백 or \n제거

# 마지막줄에 공백 출력이 됨
line='.'
while (line != ''):
    line = file.readline().rstrip() # 여기서 라인 갱신되니까 마지막줄로 갱신되고 ''인 채로 실행되겠네
    print('*'+line) #  그래서 마지막 줄 빈 문자열 참조 > print 출력 > '' + 공백 1줄('\n')이 출력


# 올바른 출력
line = file.readline() # 첫 줄 readline
while (line != ''):
    print(line.rstrip())    
    line = file.readline() # 출력 후 갱신 > 마지막 줄 빈 문자열 갱신 > while문 진입X > 공백 출력X

file.close()