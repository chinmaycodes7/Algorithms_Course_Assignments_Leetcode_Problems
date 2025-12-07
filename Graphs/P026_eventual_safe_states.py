# Auto-generated solution for P026: eventual_safe_states

from typing import List
from collections import deque

# Problem P026: Find eventual safe states
# bruteforce: detect nodes that lead to cycles via DFS (colors)
def bruteforce_eventual_safe_states(V:int, adj:List[List[int]])->List[int]:
    color=[0]*V  # 0=unvisited,1=visiting,2=safe,3=unsafe
    def dfs(u):
        if color[u]!=0:
            return color[u]==2
        color[u]=1
        for v in adj[u]:
            if color[v]==1 or not dfs(v):
                color[u]=3
                return False
        color[u]=2
        return True
    res=[]
    for i in range(V):
        if dfs(i):
            res.append(i)
    return sorted(res)

# optimized: reverse graph + Kahn's algorithm
def optimized_eventual_safe_states(V:int, adj:List[List[int]])->List[int]:
    rev=[[] for _ in range(V)]
    outdeg=[0]*V
    for u in range(V):
        for v in adj[u]:
            rev[v].append(u)
            outdeg[u]+=1
    q=deque([i for i in range(V) if outdeg[i]==0])
    safe=[False]*V
    while q:
        u=q.popleft()
        safe[u]=True
        for p in rev[u]:
            outdeg[p]-=1
            if outdeg[p]==0:
                q.append(p)
    return [i for i in range(V) if safe[i]]

def _test():
    adj=[[1,2],[2,3],[5],[0],[5],[]]
    assert bruteforce_eventual_safe_states(6,adj)==optimized_eventual_safe_states(6,adj)

if __name__=="__main__":
    _test()
    print("P026 tests passed")
