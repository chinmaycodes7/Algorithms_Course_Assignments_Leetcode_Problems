
"""P004 - Max sum subsequence with no adjacent elements"""
def top_down(arr):
    from functools import lru_cache
    n=len(arr)
    @lru_cache(None)
    def dfs(i):
        if i<0: return 0
        pick = arr[i]+dfs(i-2)
        notpick = dfs(i-1)
        return max(pick, notpick)
    return dfs(n-1)

def bottom_up(arr):
    n=len(arr)
    if n==0: return 0
    if n==1: return max(0,arr[0])
    dp=[0]*n
    dp[0]=max(0,arr[0])
    dp[1]=max(dp[0], arr[1])
    for i in range(2,n):
        dp[i]=max(dp[i-1], arr[i]+dp[i-2])
    return dp[-1]

def space_optimized(arr):
    n=len(arr)
    if n==0: return 0
    prev = max(0,arr[0])
    if n==1: return prev
    curr = max(prev, arr[1])
    for i in range(2,n):
        prev, curr = curr, max(curr, arr[i]+prev)
    return curr

if __name__=="__main__":
    assert top_down([2,1,4,9])==11
    assert bottom_up([2,1,4,9])==11
    assert space_optimized([2,1,4,9])==11
    print("P004 OK")
