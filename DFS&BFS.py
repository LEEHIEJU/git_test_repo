
# n = 3

# arr1 = [[0 for _ in range(n)] for _ in range(n)] 
# # 출력값 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# arr2 = [n * [0] for _ in range(n)]
# # 출력값 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# print(arr1)
# print(arr2) 

test_arr = [[0]*3]*3
test_arr[1] = [2,2,2] # 1번 list는 새로 정의해 줌
test_arr[2][1] = 2 # 0번, 2번 list는 아직 reference 중
print(test_arr)
# 출력값 = [[0, 2, 0], [2, 2, 2], [0, 2, 0]

# ===================================================
'''
입력 값
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# V : 정점의 개수, E : 간선의 개수 
V,E = map(int,input().split())
arr = list(map(int,input().split()))

# 인접 행렬
adj = [[0]*(V+1) for _ in range(V+1)]

# 인접 리스트
adjList = [[] for _ in range(V+1)]

for i in range(E):
    n1,n2 = arr[i*2],arr[i*2+1]
    
    adj[n1][n2] = 1 # n1과 n2 인접
    adj[n2][n1] = 1 # 방향 표시가 없는 경우

    adjList[n1].append(n2)
    adjList[n2].append(n1)


print(adj)
print()
print(adjList)



# 인접행렬은 node수에 비해 edge의 수가 적으면 적절하지않음. -> 인접리스트로 적용
# node = 7 / edge = 6
# J, G = map(int, input().split())
# arr = list(map(int, input().split()))

# # 인접리스트
# injeop_list = [[] for _ in range(J+1)]

# for i in range(G):
#     num1, num2 = arr[i*2], arr[i*2+1]
    
#     injeop_list[num1].append(num2)
#     injeop_list[num2].append(num1)
    
#     print(injeop_list)
    
# 출력값
# 7 6
# 1 2 2 3 1 5 5 2 5 6 4 7
# [[], [2], [1], [], [], [], [], []]
# [[], [2], [1, 3], [2], [], [], [], []]
# [[], [2, 5], [1, 3], [2], [], [1], [], []]
# [[], [2, 5], [1, 3, 5], [2], [], [1, 2], [], []]    
# [[], [2, 5], [1, 3, 5], [2], [], [1, 2, 6], [5], []][[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]


# G = {
    
#     1:[1,5],
#     2:[1,3,5],
#     3:[2],
#     4:[7],
#     5:[1,2,6],
#     6:[5],
#     7:[4]
    
# }