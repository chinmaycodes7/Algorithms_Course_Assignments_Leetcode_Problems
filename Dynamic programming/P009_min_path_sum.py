
"""P009 - Minimum path sum (only right and down)"""
from functools import lru_cache
def top_down(grid):
    m=len(grid); n=len(grid[0])
    @lru_cache(None)
    def dfs(i,j):
        if i==m-1 and j==n-1: return grid[i][j]
        res=10**18
        if i+1<m: res=min(res, grid[i][j]+dfs(i+1,j))
        if j+1<n: res=min(res, grid[i][j]+dfs(i,j+1))
        return res
    return dfs(0,0)

def bottom_up(grid):
    m=len(grid); n=len(grid[0])
    dp=[[10**18]*n for _ in range(m)]
    dp[m-1][n-1]=grid[m-1][n-1]
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i==m-1 and j==n-1: continue
            down = dp[i+1][j] if i+1<m else 10**18
            right = dp[i][j+1] if j+1<n else 10**18
            dp[i][j]=grid[i][j]+min(down, right)
    return dp[0][0]

def space_optimized(grid):
    m=len(grid); n=len(grid[0])
    row=[10**18]*n
    for i in range(m-1, -1, -1):
        new=[10**18]*n
        for j in range(n-1, -1, -1):
            if i==m-1 and j==n-1:
                new[j]=grid[i][j]
            else:
                down = row[j] if i+1<m else 10**18
                right = new[j+1] if j+1<n else 10**18
                new[j]=grid[i][j]+min(down, right)
        row=new
    return row[0]

if __name__=="__main__":
    g=[[1,3,1],[1,5,1],[4,2,1]]
    assert top_down(g)==7
    assert bottom_up(g)==7
    assert space_optimized(g)==7
    print("P009 OK")
