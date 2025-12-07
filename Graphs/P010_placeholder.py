# P010: Placeholder / helper for Problem 010
# The original PDF had a Problem 010 header near Problem 009 but the statement is not clearly parsed.
# I provide a canonical shortest-path helper implementation (Dijkstra) to cover typical graph uses.
# Source: Step 15 - Graphs. fileciteturn2file16

import heapq
from typing import List, Tuple

def dijkstra(n:int, edges:List[List[int]], src:int=0)->List[int]:
    g=[[] for _ in range(n)]
    for u,v,w in edges:
        g[u].append((v,w)); g[v].append((u,w))
    dist=[10**18]*n; dist[src]=0
    pq=[(0,src)]
    while pq:
        d,u=heapq.heappop(pq)
        if d>dist[u]: continue
        for v,w in g[u]:
            nd=d+w
            if nd<dist[v]:
                dist[v]=nd
                heapq.heappush(pq,(nd,v))
    return [d if d<10**17 else -1 for d in dist]

def _test():
    edges=[[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    assert dijkstra(4,edges,0)[3]==3

if __name__=="__main__":
    _test()
    print("P010 placeholder tests passed")
