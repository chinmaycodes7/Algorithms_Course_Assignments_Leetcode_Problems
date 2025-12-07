# Auto-generated solution for P040: making_large_island

from typing import List
from collections import defaultdict

# Problem P040: Making a Large Island (change at most one 0 to 1)
def bruteforce_largest_island(grid:List[List[int]])->int:
    n=len(grid)
    parent={}
    size={}
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra==rb: return
        parent[rb]=ra
        size[ra]+=size[rb]
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1:
                parent[(i,j)]=(i,j); size[(i,j)]=1
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1:
                for dx,dy in dirs:
                    ni,nj=i+dx,j+dy
                    if 0<=ni<n and 0<=nj<n and grid[ni][nj]==1:
                        if find((i,j))!=find((ni,nj)):
                            union((i,j),(ni,nj))
    ans = max(size.values()) if size else 0
    # try flipping each 0
    for i in range(n):
        for j in range(n):
            if grid[i][j]==0:
                neigh=set()
                s=1
                for dx,dy in dirs:
                    ni,nj=i+dx,j+dy
                    if 0<=ni<n and 0<=nj<n and grid[ni][nj]==1:
                        r=find((ni,nj))
                        if r not in neigh:
                            neigh.add(r)
                            s+=size[r]
                ans=max(ans,s)
    return ans

optimized_largest_island = bruteforce_largest_island

def _test():
    grid=[[1,1],[1,0]]
    assert bruteforce_largest_island(grid)==4

if __name__=="__main__":
    _test()
    print("P040 tests passed")
