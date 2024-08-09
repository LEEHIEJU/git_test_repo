import sys

while True:
    input = sys.stdin.readline()
    x,y,h = map(int,input.split())  
    if x == y == h == 0:  
        break

    if x**2 + y**2 == h**2 or y**2 + x**2 == h**2:
        print("right")
    else:
        print("wrong")
        
        # 빗변 구하기
