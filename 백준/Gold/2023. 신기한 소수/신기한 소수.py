def Prime(index, num_index, current):
    if(index == N):
        s = ""
        for num in num_index:
            s += str(num)
        print(s)
        return
    
    
    for i in range(1,10,2):
        c = str(current) + str(i)
        # print(f"c = {c}")

        flag = True
        end = int(sqrt(int(c)))
        #소수판별
        for p in range(2,end+1):
            if(int(c) % p == 0):
                flag = False
                break

        #소수라면
        if(flag):
            num_index[index] = i
            Prime(index+1, num_index, int(c))


if __name__=="__main__":
    from math import sqrt
    import sys
    input = sys.stdin.readline
    N = int(input())
    
    num_index = [0 for _ in range(N)]
    zero_index = [2,3,5,7]
    for i in zero_index:
            num_index[0] = i
            Prime(1, num_index, i)