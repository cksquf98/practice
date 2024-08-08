if __name__=="__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    loop = 2*N - 1
    star = 2*N - 1
    blank = 0
    for i in range(loop):
        print(" "*blank, end='')

        print("*"*star, end='')

        #별이랑 빈칸 수 조절
        if(i < N-1):
            blank += 1
            star -= 2
        else:
            blank -= 1
            star += 2

        print()