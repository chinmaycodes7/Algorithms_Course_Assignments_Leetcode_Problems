# Auto-generated solution for P020: number_of_islands

from typing import List

# Problem P020: Number of Islands
# bruteforce: DFS marking visited (counts islands)
def bruteforce_num_islands(grid: List[List[str]]) -> int:
    if not grid: return 0
    n,m = len(grid), len(grid[0])
    visited = [[False]*m for _ in range(n)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    def dfs(i,j):
        stack=[(i,j)]
        visited[i][j]=True
        while stack:
            x,y = stack.pop()
            for dx,dy in dirs:
                nx,ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny]=='1':
                    visited[nx][ny]=True
                    stack.append((nx,ny))
    cnt=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='1' and not visited[i][j]:
                cnt+=1
                dfs(i,j)
    return cnt

# optimized: union-find
def optimized_num_islands(grid: List[List[str]]) -> int:
    if not grid: return 0
    n,m = len(grid), len(grid[0])
    parent = {}
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    def union(a,b):
        ra,rb = find(a),find(b)
        if ra!=rb:
            parent[rb]=ra
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='1':
                parent[(i,j)]=(i,j)
    dirs = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='1':
                for dx,dy in dirs:
                    ni,nj=i+dx,j+dy
                    if 0<=ni<n and 0<=nj<m and grid[ni][nj]=='1':
                        union((i,j),(ni,nj))
    roots=set()
    for k in parent:
        roots.add(find(k))
    return len(roots)

def _test():
    g=[list("11000"), list("11000"), list("00100"), list("00011")]
    assert bruteforce_num_islands([row[:] for row in g])==3
    assert optimized_num_islands([row[:] for row in g])==3

if __name__=="__main__":
    _test()
    print("P020 tests passed")
