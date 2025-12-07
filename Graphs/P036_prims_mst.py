# Auto-generated solution for P036: prims_mst

from typing import List
import heapq

# Problem P036: Prim's Algorithm
def bruteforce_prims(V:int, edges:List[List[int]])->int:
    graph=[[] for _ in range(V)]
    for u,v,w in edges:
        graph[u].append((v,w)); graph[v].append((u,w))
    visited=[False]*V
    heap=[(0,0)]
    total=0; cnt=0
    while heap and cnt<V:
        w,u=heapq.heappop(heap)
        if visited[u]: continue
        visited[u]=True
        total+=w; cnt+=1
        for v,ww in graph[u]:
            if not visited[v]:
                heapq.heappush(heap,(ww,v))
    return total

optimized_prims = bruteforce_prims

def _test():
    edges=[[0,1,2],[0,3,6],[1,2,3],[1,3,8],[1,4,5],[4,2,7]]
    assert bruteforce_prims(5,edges)==16

if __name__=="__main__":
    _test()
    print("P036 tests passed")
