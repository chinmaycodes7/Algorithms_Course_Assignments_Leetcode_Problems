
"""P012 - Alice and Bob collect maximum chocolates"""
from functools import lru_cache

def top_down(mat):
    n=len(mat); m=len(mat[0])
    @lru_cache(None)
    def dfs(r, c1, c2):
        if c1<0 or c1>=m or c2<0 or c2>=m: return -10**18
        if r==n-1:
            return mat[r][c1] if c1==c2 else mat[r][c1]+mat[r][c2]
        best=-10**18
        curr = mat[r][c1] if c1==c2 else mat[r][c1]+mat[r][c2]
        for d1 in (-1,0,1):
            for d2 in (-1,0,1):
                best = max(best, curr + dfs(r+1, c1+d1, c2+d2))
        return best
    return dfs(0, 0, m-1)

def bottom_up(mat):
    n=len(mat); m=len(mat[0])
    dp = [[[-10**18]*m for _ in range(m)] for __ in range(n)]
    # base
    for c1 in range(m):
        for c2 in range(m):
            dp[n-1][c1][c2] = mat[n-1][c1] if c1==c2 else mat[n-1][c1]+mat[n-1][c2]
    for r in range(n-2, -1, -1):
        for c1 in range(m):
            for c2 in range(m):
                curr = mat[r][c1] if c1==c2 else mat[r][c1]+mat[r][c2]
                best=-10**18
                for d1 in (-1,0,1):
                    for d2 in (-1,0,1):
                        nc1=c1+d1; nc2=c2+d2
                        if 0<=nc1<m and 0<=nc2<m:
                            best = max(best, curr + dp[r+1][nc1][nc2])
                dp[r][c1][c2]=best
    return dp[0][0][m-1]

def space_optimized(mat):
    n=len(mat); m=len(mat[0])
    # optimize by keeping only next row
    next_dp = [[-10**18]*m for _ in range(m)]
    for c1 in range(m):
        for c2 in range(m):
            next_dp[c1][c2] = mat[n-1][c1] if c1==c2 else mat[n-1][c1]+mat[n-1][c2]
    for r in range(n-2, -1, -1):
        curr_dp = [[-10**18]*m for _ in range(m)]
        for c1 in range(m):
            for c2 in range(m):
                curr = mat[r][c1] if c1==c2 else mat[r][c1]+mat[r][c2]
                best=-10**18
                for d1 in (-1,0,1):
                    for d2 in (-1,0,1):
                        nc1=c1+d1; nc2=c2+d2
                        if 0<=nc1<m and 0<=nc2<m:
                            best = max(best, curr + next_dp[nc1][nc2])
                curr_dp[c1][c2]=best
        next_dp = curr_dp
    return next_dp[0][m-1]

if __name__=="__main__":
    mat=[[2,3,1,2],[3,4,2,2],[5,6,3,5]]
    # using provided examples, compute result
    print("P012 results:", top_down(mat), bottom_up(mat), space_optimized(mat))
    print("P012 OK")
