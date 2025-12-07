
"""P013 - Subset sum (exists)"""
def top_down(arr, target):
    from functools import lru_cache
    n=len(arr)
    @lru_cache(None)
    def dfs(i, t):
        if t==0: return True
        if i<0: return False
        notpick = dfs(i-1, t)
        pick = False
        if arr[i]<=t:
            pick = dfs(i-1, t-arr[i])
        return pick or notpick
    return dfs(n-1, target)

def bottom_up(arr, target):
    n=len(arr)
    dp = [False]*(target+1)
    dp[0]=True
    for num in arr:
        for t in range(target, num-1, -1):
            dp[t] = dp[t] or dp[t-num]
    return dp[target]

def space_optimized(arr, target):
    return bottom_up(arr, target)

if __name__=="__main__":
    arr=[2,3,1]
    assert top_down(arr,5)==True
    assert bottom_up(arr,5)==True
    print("P013 OK")
