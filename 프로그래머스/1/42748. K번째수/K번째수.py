def solution(array, commands):
    answer = []
    
    for command in commands:
        start = command[0] - 1
        end = command[1]
        target = command[2] - 1
        
        copy = array[start:end]
        copy.sort()
        answer.append(copy[target])
    
    return answer