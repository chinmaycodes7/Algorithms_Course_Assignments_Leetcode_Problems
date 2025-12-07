
"""P001 - Climbing Stairs
Ways to reach Nth stair with 1 or 2 steps.
"""
from functools import lru_cache

def top_down(n):
    @lru_cache(None)
    def dfs(i):
        if i==0 or i==1: return 1
        return dfs(i-1)+dfs(i-2)
    return dfs(n)

def bottom_up(n):
    if n==0 or n==1: return 1
    dp=[0]*(n+1)
    dp[0]=dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

def space_optimized(n):
    if n==0 or n==1: return 1
    a,b=1,1
    for _ in range(2,n+1):
        a,b = b, a+b
    return b

if __name__ == "__main__":
    cases=[(0,1),(1,1),(2,2),(3,3),(4,5),(5,8)]
    for n,exp in cases:
        assert top_down(n)==exp
        assert bottom_up(n)==exp
        assert space_optimized(n)==exp
    print("P001 OK")
