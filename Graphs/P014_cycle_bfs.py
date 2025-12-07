# P014: Detect Cycle in an Undirected Graph (BFS)
# Source: Step 15 - Graphs (Problem 014). fileciteturn2file2

from typing import List
from collections import deque

def bruteforce_cycle_bfs(V:int, edges:List[List[int]])->bool:
    # Build adjacency
    g=[[] for _ in range(V)]
    for u,v in edges:
        g[u].append(v); g[v].append(u)
    visited=[False]*V
    for i in range(V):
        if visited[i]: continue
        q=deque([(i,-1)])
        visited[i]=True
        while q:
            u,par=q.popleft()
            for v in g[u]:
                if not visited[v]:
                    visited[v]=True
                    q.append((v,u))
                elif v!=par:
                    return True
    return False

# optimized: using DSU (union-find) to detect cycle quickly
def optimized_cycle_dsu(V:int, edges:List[List[int]])->bool:
    parent=list(range(V))
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra==rb:
            return False
        parent[rb]=ra
        return True
    for u,v in edges:
        if not union(u,v):
            return True
    return False

def _test():
    assert bruteforce_cycle_bfs(8, [[0,1],[1,2],[2,3],[3,4]])==False
    assert optimized_cycle_dsu(4, [[0,1],[1,2],[2,0],[1,3]])==True

if __name__=="__main__":
    _test()
    print("P014 tests passed")
