# Auto-generated solution for P023: kahns_toposort

from typing import List
from collections import deque

# Problem P023: Kahn's Algorithm (BFS topological sort)
def bruteforce_kahn(n:int, edges:List[List[int]])->List[int]:
    indeg=[0]*n
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v)
        indeg[v]+=1
    q=deque([i for i in range(n) if indeg[i]==0])
    res=[]
    while q:
        u=q.popleft()
        res.append(u)
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:
                q.append(v)
    if len(res)!=n:
        return []
    return res

optimized_kahn = bruteforce_kahn

def _test():
    assert len(bruteforce_kahn(4, [[1,0],[2,0],[3,0]]))==4
if __name__=="__main__":
    _test()
    print("P023 tests passed")
