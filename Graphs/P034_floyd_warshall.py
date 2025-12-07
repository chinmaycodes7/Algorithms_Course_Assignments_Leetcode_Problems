# Auto-generated solution for P034: floyd_warshall

from typing import List

# Problem P034: Floyd-Warshall (in-place)
def bruteforce_floyd_warshall(mat:List[List[int]])->List[List[int]]:
    n=len(mat)
    INF=10**9
    # normalize -1 to INF (except diagonal)
    dist=[[INF]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mat[i][j]==-1 and i!=j:
                continue
            dist[i][j]=mat[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k]==INF or dist[k][j]==INF: continue
                if dist[i][j]==-1 or dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
    # convert INF back to -1 for unreachable (but preserve diagonal)
    for i in range(n):
        for j in range(n):
            if dist[i][j]>=INF//2:
                dist[i][j]=-1
    return dist

optimized_floyd_warshall = bruteforce_floyd_warshall

def _test():
    mat=[[0,2,-1,-1],[1,0,3,-1],[-1,-1,0,-1],[3,5,4,0]]
    res=bruteforce_floyd_warshall(mat)
    assert res[0][2]==5

if __name__=="__main__":
    _test()
    print("P034 tests passed")
