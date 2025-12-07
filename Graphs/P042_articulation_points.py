# Auto-generated solution for P042: articulation_points

from typing import List

# Problem P042: Articulation Points
def bruteforce_articulation_points(n:int, adj:List[List[int]])->List[int]:
    time=0
    disc=[-1]*n; low=[-1]*n; visited=[False]*n; ap=[False]*n
    def dfs(u, parent):
        nonlocal time
        visited[u]=True
        disc[u]=low[u]=time; time+=1
        children=0
        for v in adj[u]:
            if v==parent: continue
            if not visited[v]:
                children+=1
                dfs(v,u)
                low[u]=min(low[u],low[v])
                if parent!=-1 and low[v]>=disc[u]:
                    ap[u]=True
            else:
                low[u]=min(low[u],disc[v])
        if parent==-1 and children>1:
            ap[u]=True
    for i in range(n):
        if not visited[i]:
            dfs(i,-1)
    return [i for i,val in enumerate(ap) if val]

optimized_articulation_points = bruteforce_articulation_points

def _test():
    adj=[[1,2],[0,2],[0,1,3],[2]]
    assert 0 in bruteforce_articulation_points(4,adj)

if __name__=="__main__":
    _test()
    print("P042 tests passed")
