
"""P011 - Maximum path sum from top row to bottom row with moves down, down-left, down-right"""
from functools import lru_cache
def top_down(mat):
    m=len(mat); n=len(mat[0])
    @lru_cache(None)
    def dfs(i,j):
        if j<0 or j>=n: return -10**18
        if i==m-1: return mat[i][j]
        return mat[i][j] + max(dfs(i+1,j), dfs(i+1,j-1), dfs(i+1,j+1))
    best=-10**18
    for j in range(n):
        best=max(best, dfs(0,j))
    return best

def bottom_up(mat):
    m=len(mat); n=len(mat[0])
    dp=[row[:] for row in mat]
    for i in range(m-2, -1, -1):
        for j in range(n):
            down=dp[i+1][j]
            left=dp[i+1][j-1] if j-1>=0 else -10**18
            right=dp[i+1][j+1] if j+1<n else -10**18
            dp[i][j]=mat[i][j]+max(down, left, right)
    return max(dp[0])

def space_optimized(mat):
    dp=mat[-1][:]
    for i in range(len(mat)-2, -1, -1):
        new=[0]*len(mat[0])
        for j in range(len(mat[0])):
            down=dp[j]
            left=dp[j-1] if j-1>=0 else -10**18
            right=dp[j+1] if j+1<len(dp) else -10**18
            new[j]=mat[i][j]+max(down,left,right)
        dp=new
    return max(dp)

if __name__=="__main__":
    m=[[1,2,10,4],[100,3,2,1],[1,1,20,2],[1,2,2,1]]
    assert top_down(m)==105
    assert bottom_up(m)==105
    assert space_optimized(m)==105
    print("P011 OK")
