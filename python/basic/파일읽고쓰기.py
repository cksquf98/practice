'''
word.in 파일 첫번째 줄에 n,k 적혀있음
n = 에세이 단어 개수
k = 한 줄에 들어갈 수 있는 문자 수
단어 문자 개수 > K -> 개행 필요

output : 해당 형식으로 에세이 파일 출력
'''

read_file = open('python/word.in','r',encoding='utf-8')
write_file = open('python/out.in','w',encoding='utf-8')

n,k = map(int,read_file.readline().split())

line_list = []
line = '.' # split() : list로 반환 => line != '' : 이렇게 체크하면 안됨 
while line:
    line = read_file.readline().split()
    line_list.extend(line) # extend() 한쪽 리스트에 다른 리스트 추가
print(line_list)

line = ''
occupiedSpace = 0
for word in line_list:
    if(occupiedSpace + len(word) <= k):
        line = line + word + ' '
        occupiedSpace += len(word) 
    else:
        # 공간 안남음 == 그게 한 줄 완성이라는 뜻
        write_file.write(word+'\n')
        line = word + ' '
        occupiedSpace = len(word)

# 마지막 출력 라인에서 (space <= k) 만족하면 그 문장 출력이 안됨
# 따라서 한 줄 출력 코드가 또 필요함
write_file.write(line+'\n')

read_file.close()
write_file.close()