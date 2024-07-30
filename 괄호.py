# def solution(s):
import sys

v = int(sys.stdin.readline())

for i in range(v):
    stack = []
    ho = sys.stdin.readline()
    for j in ho :
        if j == "(" :          
                stack.append(j)
        elif j == ")" :  
                if stack :
                    stack.pop() 
                else:
                    print ("NO")  
                    break
    else:         
        if len(stack) == 0 : 
            print("Yes")
        else :
            print("NO")
            
