
"""P015 - Minimum subset sum difference"""
def min_partition_diff(arr):
    total=sum(arr)
    target=total//2
    dp=[False]*(target+1)
    dp[0]=True
    for num in arr:
        for t in range(target, num-1, -1):
            dp[t]=dp[t] or dp[t-num]
    best=10**18
    for s in range(target+1):
        if dp[s]:
            best=min(best, abs(total-2*s))
    return best

if __name__=="__main__":
    assert min_partition_diff([1,6,11,5])==1
    print("P015 OK")
