# Auto-generated solution for P033: bellman_ford

from typing import List

# Problem P033: Bellman-Ford
def bruteforce_bellman_ford(V:int, edges:List[List[int]], S:int)->List[int]:
    INF=10**18
    dist=[INF]*V
    dist[S]=0
    for _ in range(V-1):
        for u,v,w in edges:
            if dist[u]!=INF and dist[v]>dist[u]+w:
                dist[v]=dist[u]+w
    # check negative cycle
    for u,v,w in edges:
        if dist[u]!=INF and dist[v]>dist[u]+w:
            return [-1]
    return dist

optimized_bellman_ford = bruteforce_bellman_ford

def _test():
    edges=[[3,2,6],[5,3,1],[0,1,5],[1,5,-3],[1,2,-2],[3,4,-2],[2,4,3]]
    assert bruteforce_bellman_ford(6,edges,0)[0]==0

if __name__=="__main__":
    _test()
    print("P033 tests passed")
