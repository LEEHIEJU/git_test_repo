
import sys

# 인접행렬은 node수에 비해 edge의 수가 적으면 적절하지않음. -> 인접리스트로 적용
# node = 7 / edge = 6

        
node = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

# 인접리스트 초기화
G = [[] for _ in range(node+1)]

# print("edge 입력 :")

# edge를 알기위해 반복문 돌린다.
for _ in range(edge):
    x, y = map(int,sys.stdin.readline().split()) # 연결된 값은 리스트로
    
    # 양방향
    G[x].append(y)
    G[y].append(x)
    
# node 카운트를 초기화하고 
count = 0
visited = [False for _ in range(node+1)]


def DFS(i):
    
    global count
    # 방문한 node일 경우 True
    visited[i] = [True]
    # i값에 대한 반복문을 돌려서 
    for n in G[i]:
        # print(n)
        if not visited[n]:
            # 만약 해당 node가 방문하지않으면 
            count += 1
            # count +1
            DFS(n)
        
        # print("visite : ", visited)
        # print(n)
        # print(count)
DFS(1)
print(count)
# print(count)
# print("방문한 노드의 수 : ", count)


    

