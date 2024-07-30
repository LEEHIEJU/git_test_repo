import sys

q = int(sys.stdin.readline())
queue = []

for i in range(q):
    u = sys.stdin.readline().split()
    if u[0] == "push":
        queue.append(u[1])
        
    elif u[0] == "size":        
            print(len(queue))
            
    elif u[0] == "empty" :
            if len(queue) == 0:        
                print(1)
            else: print(0)
        
    elif u[0] == "front":      
            if len(queue) == 0 :        
                print(-1)
            else: print(queue[0])
            
    elif u[0] == "back":
        if len(queue) == 0:
            print(-1)
        else: print(queue[-1])         
            
    elif u[0] == "pop" :       
            if len(queue) > 0 :         
                print(queue.pop())
            else:  print(-1)           