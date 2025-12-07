
"""P003 - Frog K (min energy up to K steps)"""
from functools import lru_cache

def top_down(heights, k):
    n=len(heights)
    @lru_cache(None)
    def dfs(i):
        if i==0: return 0
        ans=10**18
        for jump in range(1, min(k,i)+1):
            ans = min(ans, dfs(i-jump)+abs(heights[i]-heights[i-jump]))
        return ans
    return dfs(n-1)

def bottom_up(heights, k):
    n=len(heights)
    dp=[10**18]*n
    dp[0]=0
    for i in range(1,n):
        for j in range(1, min(k,i)+1):
            dp[i]=min(dp[i], dp[i-j]+abs(heights[i]-heights[i-j]))
    return dp[-1]

def space_optimized(heights, k):
    # we still need last k values; use deque-like circular buffer
    from collections import deque
    n=len(heights)
    dp=[0]
    for i in range(1,n):
        best=10**18
        upto = min(k, i)
        for j in range(1, upto+1):
            best=min(best, dp[i-j]+abs(heights[i]-heights[i-j]))
        dp.append(best)
    return dp[-1]

if __name__=="__main__":
    h=[10,20,30,10]
    assert top_down(h,2)==20
    assert bottom_up(h,2)==20
    assert space_optimized(h,2)==20
    # k=3
    assert top_down(h,3)==10
    assert bottom_up(h,3)==10
    assert space_optimized(h,3)==10
    print("P003 OK")
