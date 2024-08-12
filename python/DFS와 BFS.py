from collections import deque
import stack
import sys

input = sys.stdin.readline()

node, edge, swing  = map(int, input.split()) # 입력값 구함
n, e = list(map(int, input.split())) # 노드에 따른 엣지 리스트 입력

# BFS 반복
def bfs(graph, root):
    visited = []
    queue = deque([root])
    
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += n[n]-set(e)
            
        return visited

# DFS 반복
def dfs(graph, root):
    visited = []
    stack

