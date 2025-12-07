
"""P007 - Unique paths in MxN grid (only right and down)"""
from functools import lru_cache
def top_down(m,n):
    @lru_cache(None)
    def dfs(i,j):
        if i==m-1 and j==n-1: return 1
        if i>=m or j>=n: return 0
        return dfs(i+1,j)+dfs(i,j+1)
    return dfs(0,0)

def bottom_up(m,n):
    dp=[[0]*n for _ in range(m)]
    dp[m-1][n-1]=1
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i==m-1 and j==n-1: continue
            right = dp[i][j+1] if j+1<n else 0
            down = dp[i+1][j] if i+1<m else 0
            dp[i][j]=right+down
    return dp[0][0]

def space_optimized(m,n):
    # use single row
    row=[0]*n
    row[n-1]=1
    for i in range(m-1, -1, -1):
        new=[0]*n
        for j in range(n-1, -1, -1):
            if i==m-1 and j==n-1:
                new[j]=1
            else:
                right = new[j+1] if j+1<n else 0
                down = row[j] if i+1<m else 0
                new[j]=right+down
        row=new
    return row[0]

if __name__=="__main__":
    assert top_down(3,3)==6
    assert bottom_up(3,3)==6
    assert space_optimized(3,3)==6
    print("P007 OK")
