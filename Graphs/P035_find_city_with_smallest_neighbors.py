# Auto-generated solution for P035: find_city_with_smallest_neighbors

from typing import List
import heapq

# Problem P035: Find the city with smallest number of reachable cities within threshold
def bruteforce_find_city(n:int, edges:List[List[int]], distanceThreshold:int)->int:
    # use Dijkstra from each node (since n up to moderate)
    graph=[[] for _ in range(n)]
    for u,v,w in edges:
        graph[u].append((v,w)); graph[v].append((u,w))
    def dijkstra(src):
        dist=[10**9]*n
        dist[src]=0
        heap=[(0,src)]
        while heap:
            d,u=heapq.heappop(heap)
            if d>dist[u]: continue
            for v,w in graph[u]:
                nd=d+w
                if nd<dist[v]:
                    dist[v]=nd
                    heapq.heappush(heap,(nd,v))
        return dist
    best_count=10**9; ans=-1
    for i in range(n):
        dist=dijkstra(i)
        cnt=sum(1 for d in dist if d<=distanceThreshold and d>0)
        if cnt<=best_count:
            best_count=cnt; ans=i
    return ans

optimized_find_city = bruteforce_find_city

def _test():
    edges=[[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    assert bruteforce_find_city(4,edges,4)==3

if __name__=="__main__":
    _test()
    print("P035 tests passed")
