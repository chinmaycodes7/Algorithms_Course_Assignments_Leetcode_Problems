
"""P014 - Partition equal subset sum"""
def can_partition(arr):
    total=sum(arr)
    if total%2!=0: return False
    target=total//2
    # reuse subset sum DP
    dp=[False]*(target+1)
    dp[0]=True
    for num in arr:
        for t in range(target, num-1, -1):
            dp[t]=dp[t] or dp[t-num]
    return dp[target]

if __name__=="__main__":
    assert can_partition([1,5,11,5])==True
    assert can_partition([1,2,3,5])==False
    print("P014 OK")
