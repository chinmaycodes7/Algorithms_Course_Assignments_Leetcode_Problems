# Auto-generated solution for P031: cheapest_flights_k_stops

from typing import List

# Problem P031: Cheapest Flights Within K Stops
def bruteforce_cheapest_flights(n:int, flights:List[List[int]], src:int, dst:int, K:int)->int:
    # DP over stops (Bellman-Ford limited to K+1 iterations)
    INF=10**9
    dist=[INF]*n
    dist[src]=0
    for _ in range(K+1):
        new=dist[:]
        for u,v,w in flights:
            if dist[u]==INF: continue
            if new[v]>dist[u]+w:
                new[v]=dist[u]+w
        dist=new
    return dist[dst] if dist[dst]!=INF else -1

optimized_cheapest_flights = bruteforce_cheapest_flights

def _test():
    flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    assert bruteforce_cheapest_flights(4,flights,0,3,1)==700

if __name__=="__main__":
    _test()
    print("P031 tests passed")
