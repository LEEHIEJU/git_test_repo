import sys

while True:
    input = sys.stdin.readline()
    x,y,h = map(int,input.split())  
    if x == y == h == 0:  
        break
    
    a, b, c = sorted([x, y, h]) 
    # 오름차순으로 정렬해서 항상 c가 더 큰 수로 나올 수 있게 출력
    
    if a**2 + b**2 == c**2 :
        print("right")
    else:
        print("wrong")
