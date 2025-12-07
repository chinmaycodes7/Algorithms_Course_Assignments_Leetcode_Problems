# Auto-generated solution for P039: num_islands_online_queries

from typing import List

# Problem P039: Number of Islands - II (online queries)
def bruteforce_num_islands_ii(n:int,m:int,ops:List[List[int]])->List[int]:
    parent={}
    rank={}
    grid=[[0]*m for _ in range(n)]
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra==rb: return False
        if rank[ra]<rank[rb]:
            parent[ra]=rb
        elif rank[ra]>rank[rb]:
            parent[rb]=ra
        else:
            parent[rb]=ra; rank[ra]+=1
        return True
    res=[]
    count=0
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    for x,y in ops:
        if grid[x][y]==1:
            res.append(count); continue
        grid[x][y]=1
        idx=(x,y)
        parent[idx]=idx; rank[idx]=0
        count+=1
        for dx,dy in dirs:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and grid[nx][ny]==1:
                if union(idx,(nx,ny)):
                    count-=1
        res.append(count)
    return res

optimized_num_islands_ii = bruteforce_num_islands_ii

def _test():
    assert bruteforce_num_islands_ii(4,5,[[1,1],[0,1],[3,3],[3,4]])==[1,1,2,2]

if __name__=="__main__":
    _test()
    print("P039 tests passed")
