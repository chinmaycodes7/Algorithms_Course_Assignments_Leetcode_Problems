# Auto-generated solution for P022: topological_sort

from typing import List

# Problem P022: Topological Sort (DFS)
def bruteforce_toposort(n:int, edges:List[List[int]])->List[int]:
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v)
    visited=[False]*n
    res=[]
    def dfs(u):
        visited[u]=True
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
        res.append(u)
    for i in range(n):
        if not visited[i]:
            dfs(i)
    return res[::-1]

optimized_toposort = bruteforce_toposort

def _test():
    assert bruteforce_toposort(6, [[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]]) in ([5,4,2,3,1,0],[4,5,2,3,1,0])
if __name__=="__main__":
    _test()
    print("P022 tests passed")
