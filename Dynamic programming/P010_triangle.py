
"""P010 - Triangle minimum path sum"""
def top_down(triangle):
    from functools import lru_cache
    n=len(triangle)
    @lru_cache(None)
    def dfs(i,j):
        if i==n-1: return triangle[i][j]
        return triangle[i][j] + min(dfs(i+1,j), dfs(i+1,j+1))
    return dfs(0,0)

def bottom_up(triangle):
    n=len(triangle)
    dp = [row[:] for row in triangle]
    for i in range(n-2, -1, -1):
        for j in range(len(triangle[i])):
            dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
    return dp[0][0]

def space_optimized(triangle):
    dp = triangle[-1][:]
    for i in range(len(triangle)-2, -1, -1):
        new=[0]*len(triangle[i])
        for j in range(len(triangle[i])):
            new[j] = triangle[i][j] + min(dp[j], dp[j+1])
        dp=new
    return dp[0]

if __name__=="__main__":
    tri=[[2],[3,4],[6,5,7],[4,1,8,3]]
    assert top_down(tri)==11
    assert bottom_up(tri)==11
    assert space_optimized(tri)==11
    print("P010 OK")
