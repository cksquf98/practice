def Find(num):
    if(parents[num] != num):
        parents[num] = Find(parents[num])
    
    return parents[num]

def Union(num1, num2):
    num1_parents = Find(num1)
    num2_parents = Find(num2)
    
    if(num1_parents != num2_parents):
        parents[num2_parents] = num1_parents #아 이걸 parents[num]으로 하면 안되지 허허




if __name__=="__main__":
    import sys
    input = sys.stdin.readline
    
    n,m = map(int, input().split())
    parents = [i for i in range(n+1)]

    for _ in range(m):
        op, num1, num2 = map(int, input().split())
        if(op == 0):
            # Union
            Union(num1, num2)

        else:
            # op == 1 :같은 집합인지 여부 출력
            if(Find(num1) == Find(num2)):
                print("YES")

            else:
                print("NO")