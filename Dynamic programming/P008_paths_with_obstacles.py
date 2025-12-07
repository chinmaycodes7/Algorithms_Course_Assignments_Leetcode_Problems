
"""P008 - Unique paths with obstacles (-1 denotes blockage)"""
from functools import lru_cache
def top_down(grid):
    m=len(grid); n=len(grid[0])
    @lru_cache(None)
    def dfs(i,j):
        if i<0 or j<0 or i>=m or j>=n: return 0
        if grid[i][j]==-1: return 0
        if i==m-1 and j==n-1: return 1
        return dfs(i+1,j)+dfs(i,j+1)
    return dfs(0,0)

def bottom_up(grid):
    m=len(grid); n=len(grid[0])
    dp=[[0]*n for _ in range(m)]
    if grid[m-1][n-1]==-1: return 0
    dp[m-1][n-1]=1
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if grid[i][j]==-1: dp[i][j]=0; continue
            if i==m-1 and j==n-1: continue
            down = dp[i+1][j] if i+1<m else 0
            right = dp[i][j+1] if j+1<n else 0
            dp[i][j]=down+right
    return dp[0][0]

def space_optimized(grid):
    m=len(grid); n=len(grid[0])
    row=[0]*n
    if grid[m-1][n-1]==-1: return 0
    row[n-1]=1
    for i in range(m-1, -1, -1):
        new=[0]*n
        for j in range(n-1, -1, -1):
            if grid[i][j]==-1:
                new[j]=0; continue
            if i==m-1 and j==n-1:
                new[j]=1
            else:
                down = row[j] if i+1<m else 0
                right = new[j+1] if j+1<n else 0
                new[j]=down+right
        row=new
    return row[0]

if __name__=="__main__":
    g=[[0,0,0],[0,-1,0],[0,0,0]]
    assert top_down(g)==2
    assert bottom_up(g)==2
    assert space_optimized(g)==2
    print("P008 OK")
