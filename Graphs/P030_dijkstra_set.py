# Auto-generated solution for P030: dijkstra_set

import heapq
from typing import List

# Problem P030: Dijkstra's algorithm (set/priority queue)
def bruteforce_dijkstra(V:int, adj:List[List[List[int]]], S:int)->List[int]:
    # adj format: list of list of [neighbor, weight]
    dist=[10**18]*V
    dist[S]=0
    heap=[(0,S)]
    while heap:
        d,u=heapq.heappop(heap)
        if d>dist[u]: continue
        for v,w in adj[u]:
            if dist[v]>d+w:
                dist[v]=d+w
                heapq.heappush(heap,(dist[v],v))
    return dist

optimized_dijkstra = bruteforce_dijkstra

def _test():
    adj=[[[1,9]], [[0,9]]]
    assert bruteforce_dijkstra(2,adj,0)==[0,9]

if __name__=="__main__":
    _test()
    print("P030 tests passed")
