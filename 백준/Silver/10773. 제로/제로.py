import sys

N = int(sys.stdin.readline())
st = []  #파이썬은 스택 대신 리스트를 활용

for i in range(N):
    num = int(sys.stdin.readline())
    if(num == 0 and len(st) != 0):
        st.pop()
    else:
        st.append(num)

count = 0
for i in st:
    count += i

print(count)