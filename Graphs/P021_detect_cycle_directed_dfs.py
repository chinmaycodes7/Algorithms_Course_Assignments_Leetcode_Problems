# Auto-generated solution for P021: detect_cycle_directed_dfs

from typing import List

# Problem P021: Detect cycle in directed graph (DFS)
def bruteforce_detect_cycle_directed(n:int, edges:List[List[int]])->bool:
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v)
    visited=[0]*n
    def dfs(u):
        visited[u]=1
        for v in adj[u]:
            if visited[v]==1:
                return True
            if visited[v]==0 and dfs(v):
                return True
        visited[u]=2
        return False
    for i in range(n):
        if visited[i]==0 and dfs(i):
            return True
    return False

optimized_detect_cycle_directed = bruteforce_detect_cycle_directed

def _test():
    assert bruteforce_detect_cycle_directed(4, [[0,1],[1,2],[2,0]])==True
    assert bruteforce_detect_cycle_directed(3, [[0,1],[1,2]])==False

if __name__=="__main__":
    _test()
    print("P021 tests passed")
