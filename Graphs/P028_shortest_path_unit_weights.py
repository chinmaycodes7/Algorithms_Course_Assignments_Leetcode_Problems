# Auto-generated solution for P028: shortest_path_unit_weights

from collections import deque
from typing import List

# Problem P028: Shortest Path in Undirected Graph with unit distance
def bruteforce_shortest_unit(n:int, edges:List[List[int]])->List[int]:
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v); adj[v].append(u)
    INF=10**9
    dist=[INF]*n
    dist[0]=0
    q=deque([0])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if dist[v]>dist[u]+1:
                dist[v]=dist[u]+1
                q.append(v)
    return [d if d<INF else -1 for d in dist]

optimized_shortest_unit = bruteforce_shortest_unit

def _test():
    edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]]
    assert bruteforce_shortest_unit(9,edges)[0]==0

if __name__=="__main__":
    _test()
    print("P028 tests passed")
