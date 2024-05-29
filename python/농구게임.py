apple = 0
banana = 0
i=0

while(i<6):
    score = int(input('write down your score : '))
    if( 0 > score or score >100 ):
        print('wrong score form')
    else:
        if(i==1):
            apple += score*3
            i+=1
        elif(i==6 or i==3):
            apple += score
            i+=1
        elif(i==2):
            apple += score*2
            i+=1
        elif(i==4):
            banana += score*3
            i+=1
        else:
            banana += score*2
            i+=1

if(apple > banana):
    print('A')
elif( banana > apple):
    print('B')
else:
    print('T')