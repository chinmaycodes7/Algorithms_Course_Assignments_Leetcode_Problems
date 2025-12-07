# P009: Number of Ways to Arrive at Destination
# Source: Step 15 - Graphs (Problem 009). fileciteturn2file16
# Bruteforce: run Dijkstra-like process without optimizations (still uses heap)
# Optimized: Standard Dijkstra counting shortest paths with modulo

import heapq
from typing import List

MOD = 10**9 + 7

def bruteforce_count_ways(n:int, roads:List[List[int]])->int:
    # Build graph and run Dijkstra keeping count of ways (straightforward)
    g=[[] for _ in range(n)]
    for u,v,w in roads:
        g[u].append((v,w)); g[v].append((u,w))
    dist=[10**18]*n
    ways=[0]*n
    dist[0]=0; ways[0]=1
    pq=[(0,0)]
    while pq:
        d,u=heapq.heappop(pq)
        if d>dist[u]: continue
        for v,w in g[u]:
            nd=d+w
            if nd<dist[v]:
                dist[v]=nd
                ways[v]=ways[u]
                heapq.heappush(pq,(nd,v))
            elif nd==dist[v]:
                ways[v]=(ways[v]+ways[u])%MOD
    return ways[n-1]%MOD if dist[n-1]<10**17 else 0

# optimized is the same algorithm (this problem's canonical solution)
optimized_count_ways = bruteforce_count_ways

def _test():
    n=7
    roads=[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    assert bruteforce_count_ways(n,roads)==4
    n=6
    roads=[[0,5,8],[0,2,2],[0,1,1],[1,3,3],[1,2,3],[2,5,6],[3,4,2],[4,5,2]]
    assert optimized_count_ways(n,roads)==3

if __name__=="__main__":
    _test()
    print("P009 tests passed")
