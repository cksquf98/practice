import sys
import math

input = sys.stdin.readline

row, col, vertical, horizon = map(int, input().split())

# 세로줄에 들어갈 사람 수
row_person_count = math.ceil(row / (vertical + 1))

# 가로줄에 들어갈 사람 수
col_person_count = math.ceil(col / (horizon + 1))

print(row_person_count * col_person_count)