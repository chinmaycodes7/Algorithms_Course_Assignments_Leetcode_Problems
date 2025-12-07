# Auto-generated solution for P043: kosaraju_scc

from typing import List

# Problem P043: Strongly Connected Components - Kosaraju's algorithm
def bruteforce_kosaraju(V:int, edges:List[List[int]])->int:
    adj=[[] for _ in range(V)]
    radj=[[] for _ in range(V)]
    for u,v in edges:
        adj[u].append(v); radj[v].append(u)
    visited=[False]*V; order=[]
    def dfs(u):
        visited[u]=True
        for v in adj[u]:
            if not visited[v]: dfs(v)
        order.append(u)
    for i in range(V):
        if not visited[i]: dfs(i)
    visited=[False]*V
    comp=0
    def dfs2(u):
        visited[u]=True
        for v in radj[u]:
            if not visited[v]: dfs2(v)
    for u in reversed(order):
        if not visited[u]:
            dfs2(u)
            comp+=1
    return comp

optimized_kosaraju = bruteforce_kosaraju

def _test():
    edges=[[0,1],[1,2],[2,0],[1,3]]
    assert bruteforce_kosaraju(4,edges)==2

if __name__=="__main__":
    _test()
    print("P043 tests passed")
