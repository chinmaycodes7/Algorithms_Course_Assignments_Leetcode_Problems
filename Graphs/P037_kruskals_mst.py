# Auto-generated solution for P037: kruskals_mst

from typing import List

# Problem P037: Kruskal's Algorithm
def bruteforce_kruskal(V:int, edges:List[List[int]])->int:
    parent=list(range(V))
    rank=[0]*V
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra==rb: return False
        if rank[ra]<rank[rb]:
            parent[ra]=rb
        elif rank[rb]<rank[ra]:
            parent[rb]=ra
        else:
            parent[rb]=ra; rank[ra]+=1
        return True
    edges_sorted=sorted(edges,key=lambda x:x[2])
    total=0
    for u,v,w in edges_sorted:
        if union(u,v):
            total+=w
    return total

optimized_kruskal = bruteforce_kruskal

def _test():
    edges=[[0,1,2],[0,3,6],[1,2,3],[1,3,8],[1,4,5],[4,2,7]]
    assert bruteforce_kruskal(5,edges)==16

if __name__=="__main__":
    _test()
    print("P037 tests passed")
