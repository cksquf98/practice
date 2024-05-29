import sys

#최대공약수
def maxDiv(a,b):
    if(a > b):
        while(b > 0):
            rest = a % b
            if(rest == 0):   return b
            a = b
            b = rest
    else:
        while(a > 0):
            rest = b % a
            if(rest == 0):   return a
            b = a
            a = rest


N = int(sys.stdin.readline())
interval = []

num1 = int(sys.stdin.readline())
for i in range(N-1):
    num2 = int(sys.stdin.readline())
    interval.append(num2-num1)
    num1 = num2

divisor = maxDiv(interval[0],interval[1])
for i in range(2,N-1):
    divisor = maxDiv(divisor, interval[2])

count = 0
for i in interval:
    count += i/divisor -1

print(int(count))