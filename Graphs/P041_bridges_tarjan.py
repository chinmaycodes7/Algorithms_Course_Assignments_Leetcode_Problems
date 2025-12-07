# Auto-generated solution for P041: bridges_tarjan

from typing import List

# Problem P041: Bridges (Tarjan)
def bruteforce_bridges(n:int, connections:List[List[int]])->List[List[int]]:
    adj=[[] for _ in range(n)]
    for u,v in connections:
        adj[u].append(v); adj[v].append(u)
    time=0
    disc=[-1]*n; low=[-1]*n; visited=[False]*n
    res=[]
    def dfs(u, parent):
        nonlocal time
        visited[u]=True
        disc[u]=low[u]=time; time+=1
        for v in adj[u]:
            if v==parent: continue
            if not visited[v]:
                dfs(v,u)
                low[u]=min(low[u],low[v])
                if low[v]>disc[u]:
                    res.append([u,v])
            else:
                low[u]=min(low[u],disc[v])
    for i in range(n):
        if not visited[i]:
            dfs(i,-1)
    return res

optimized_bridges = bruteforce_bridges

def _test():
    assert bruteforce_bridges(4, [[0,1],[1,2],[2,0],[1,3]])==[[1,3]]

if __name__=="__main__":
    _test()
    print("P041 tests passed")
