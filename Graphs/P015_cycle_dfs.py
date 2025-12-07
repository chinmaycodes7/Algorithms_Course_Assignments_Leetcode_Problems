# P015: Detect Cycle in an Undirected Graph (DFS)
# Source: Step 15 - Graphs (Problem 015). fileciteturn2file2

from typing import List

def bruteforce_cycle_dfs(V:int, edges:List[List[int]])->bool:
    g=[[] for _ in range(V)]
    for u,v in edges:
        g[u].append(v); g[v].append(u)
    visited=[False]*V
    def dfs(u,par):
        visited[u]=True
        for v in g[u]:
            if not visited[v]:
                if dfs(v,u): return True
            elif v!=par:
                return True
        return False
    for i in range(V):
        if not visited[i] and dfs(i,-1):
            return True
    return False

optimized_cycle_dfs = bruteforce_cycle_dfs

def _test():
    assert bruteforce_cycle_dfs(8, [[0,1],[1,2],[2,3],[3,4]])==False
    assert optimized_cycle_dfs(4, [[0,1],[1,2],[2,0],[1,3]])==True

if __name__=="__main__":
    _test()
    print("P015 tests passed")
