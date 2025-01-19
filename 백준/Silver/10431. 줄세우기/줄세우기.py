import sys
input = sys.stdin.readline

P = int(input())

for i in range(1,P+1):
    input_list = list(map(int, input().rstrip().split(' ')))
    students = input_list[1:]

    total = 0
    for index in range(20):
        target = students[index]

        for prev_index in range(0, index):
            if(students[prev_index] < target):
                continue
            else:
                students.remove(target)
                students.insert(prev_index, target)
                total += index - prev_index
                break

    print(f"{input_list[0]} {total}")