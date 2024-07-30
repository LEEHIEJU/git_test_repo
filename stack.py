
# def stack_hiz():

import sys 
          
v = int(sys.stdin.readline())      
stack = []                          
    
for i in range(v):
        s = sys.stdin.readline().split()   
        if s[0] == "push" :               
            stack.append(s[1])
    
        elif s[0] == "size":        
            print(len(stack))
        
        elif s[0] == "empty" :
            if len(stack) == 0:        
                print(1)
            else: print(0)
        
        elif s[0] == "top":      
            if len(stack) == 0 :        
                print(-1)
            else: print(stack[-1]) 
            
        elif s[0] == "pop" :       
            if len(stack) > 0 :         
                print(stack.pop())
            else:  print(-1)
            
            """
    class Stack:

    def init(self):
        self.top = []  
    def len(self):
        return len(self.top)  
# items = list(int(), input().split)
            
    def push(self, data):
            print(self.items.append(data)) # 정수 data를 스택에 넣는 연산

    def top(self, data):
        if len(self.items) == 0 : # 비어있으면 -1을 출력
            print(-1)
        else :
            print(self.items[-1])     # 아니면 가장 위에있는 정수 출력

    def pop(self):                      # 스택에서 가장 위에있는 정수를 빼고, 그 수를 출력한다.
        pop_objeck = None
        if self.top is None:            # 만약 정수가 없으면
            print(-1)                   # -1를 출력한다.
        else:
            pop_objeck = self.items.pop()
            print(pop_objeck)
            
    def size(self):             # stack에 들어있는 정수의개수를 출력
        print()

    def empty(self):             # empty
        if len(self.items) == 0: # 비어있으면 1을 출력 아니면 0을 출력하라
            print(1)
        else:
            print(0)  """
            
            
#             # def solution(s):
# v = int(input())
# for i in range(v):
#     stack = []
#     gual = input()
#     # ho = sys.stdin.readline().split()
# for j in gual:
#     if j == "(":          # 해당 값이 들어오면
#             stack.append(v) # stack에 값을 저장
#     elif j == ")":         # 해당 값이 들어오면
#             if len(stack) != 0:
#                 stack.pop       # 맨 마지막 값을 꺼내온다.
#             print("YES")    
#     else:  
#         print("No")
#     break
#     # else:
#     #          print("No")
#     #          break          # break
# else:         
#              if len(stack) == 0 : # stack이 비어있으면
#                  print("Yes")
#              else :
#                  print("No")
            
#         #     print("")
#         #     print(stack)
#         #     print("==================")
#         # elif ho == ")":
#         #     stack.pop(i)
#         #     print(stack)
#         #     if len(stack) == 0:
#         #         break
            
#            # if not stack:
#             #    print("No")
#             #else:
    
    
        