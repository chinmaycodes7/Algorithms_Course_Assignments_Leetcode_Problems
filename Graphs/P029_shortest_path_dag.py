# Auto-generated solution for P029: shortest_path_dag

from typing import List
from collections import deque

# Problem P029: Shortest Path in DAG (weighted)
def bruteforce_shortest_path_dag(n:int, edges:List[List[int]])->List[int]:
    adj=[[] for _ in range(n)]
    indeg=[0]*n
    for u,v,w in edges:
        adj[u].append((v,w)); indeg[v]+=1
    # topological sort
    q=deque([i for i in range(n) if indeg[i]==0])
    topo=[]
    while q:
        u=q.popleft(); topo.append(u)
        for v,_ in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:
                q.append(v)
    INF=10**9
    dist=[INF]*n
    dist[0]=0
    for u in topo:
        if dist[u]!=INF:
            for v,w in adj[u]:
                if dist[v]>dist[u]+w:
                    dist[v]=dist[u]+w
    for i in range(n):
        if dist[i]==INF: dist[i]=-1
    return dist

optimized_shortest_path_dag = bruteforce_shortest_path_dag

def _test():
    edges=[[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
    assert bruteforce_shortest_path_dag(6,edges)[3]==6

if __name__=="__main__":
    _test()
    print("P029 tests passed")
