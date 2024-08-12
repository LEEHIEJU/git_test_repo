import sys

input = sys.stdin.readline

x = int(input())
count = 0

while x > 0:
    if x % 5 == 0 : # 5로 나눈 나머지가 0이면
        count += x//5 # 5로 나눈 몫을 count
        break 
    x -= 2 # 입력값에서 2를 지우고
    count += 1 # +1
if x >= 0:
    print(count)
else:
    print(-1)
    
        