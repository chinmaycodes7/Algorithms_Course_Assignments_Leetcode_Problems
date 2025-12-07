
"""P002 - Frog 1 (min energy)"""
from functools import lru_cache
def top_down(heights):
    n=len(heights)
    @lru_cache(None)
    def dfs(i):
        if i==0: return 0
        res = dfs(i-1)+abs(heights[i]-heights[i-1])
        if i>1:
            res = min(res, dfs(i-2)+abs(heights[i]-heights[i-2]))
        return res
    return dfs(n-1)

def bottom_up(heights):
    n=len(heights)
    dp=[0]*n
    dp[0]=0
    for i in range(1,n):
        dp[i]=dp[i-1]+abs(heights[i]-heights[i-1])
        if i>1:
            dp[i]=min(dp[i], dp[i-2]+abs(heights[i]-heights[i-2]))
    return dp[-1]

def space_optimized(heights):
    n=len(heights)
    if n==1: return 0
    prev=0
    curr=abs(heights[1]-heights[0])
    if n==2: return curr
    for i in range(2,n):
        nxt = min(curr+abs(heights[i]-heights[i-1]), prev+abs(heights[i]-heights[i-2]))
        prev, curr = curr, nxt
    return curr

if __name__=="__main__":
    h=[10,20,30,10]
    assert top_down(h)==20
    assert bottom_up(h)==20
    assert space_optimized(h)==20
    print("P002 OK")
