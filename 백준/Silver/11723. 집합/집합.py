import sys
input = sys.stdin.readline

my_set = set()

M = int(input())

for _ in range(M):
    inputLine = input().rstrip()
    if (' ' in inputLine):
        command, num = inputLine.split(' ')
        num = int(num)
        if command == 'add':
            my_set.add(num)
        elif command == 'remove':
            my_set.discard(num)
        elif command == 'check':
            if (num in my_set):
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if (num in my_set):
                my_set.remove(num)
            else:
                my_set.add(num)

    elif inputLine == 'all':
        my_set.update(i for i in range(1,21))
    else:
        my_set = set()

# set 내장객체 이름 중복땜시